# importing python libraries and modules
import csv, json, os # modules built into Python (no install needed)
import re
import secrets
import sqlite3
from contextlib import closing
from datetime import datetime, timezone
from flask import Flask, g, jsonify, request, send_from_directory, session # tools taken from the Flask library
from werkzeug.security import check_password_hash, generate_password_hash
#creating the application and setting up the session cookie
app = Flask(__name__) # create the web application
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or secrets.token_hex(32)
app.config.update(
	SESSION_COOKIE_HTTPONLY=True,
	SESSION_COOKIE_SAMESITE="Lax",
	SESSION_COOKIE_SECURE=os.environ.get("FLASK_COOKIE_SECURE") == "1",
)

# feedback for the website - where it is stored 
FEEDBACK_FILE = os.environ.get("FEEDBACK_FILE", os.path.join(app.root_path, "feedback.csv"))
ACCOUNT_DB = os.environ.get("ACCOUNT_DB", os.path.join(app.root_path, "accounts.sqlite3"))

# creating the database for the accounts and activities
def init_account_db():
	os.makedirs(os.path.dirname(os.path.abspath(ACCOUNT_DB)), exist_ok=True)
	with closing(sqlite3.connect(ACCOUNT_DB)) as database:
		database.execute("PRAGMA foreign_keys = ON")
		database.executescript("""
			CREATE TABLE IF NOT EXISTS users (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				username TEXT NOT NULL COLLATE NOCASE UNIQUE,
				password_hash TEXT NOT NULL
			);
			CREATE TABLE IF NOT EXISTS activity_records (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				user_id INTEGER NOT NULL REFERENCES users(id),
				activity TEXT NOT NULL,
				season TEXT NOT NULL,
				done_at TEXT NOT NULL
			);
		""")
		database.commit()
		columns = {row[1] for row in database.execute("PRAGMA table_info(activity_records)")}
		if "activity_key" not in columns:
			database.execute("ALTER TABLE activity_records ADD COLUMN activity_key TEXT")
		database.execute(
			"CREATE UNIQUE INDEX IF NOT EXISTS idx_activity_records_user_key "
			"ON activity_records (user_id, activity_key) WHERE activity_key IS NOT NULL"
		)
		database.commit()
	os.chmod(ACCOUNT_DB, 0o600)

# getting the database for the accounts and activities
def get_account_db():
	if "account_db" not in g:
		g.account_db = sqlite3.connect(ACCOUNT_DB, timeout=5)
		g.account_db.row_factory = sqlite3.Row
		g.account_db.execute("PRAGMA foreign_keys = ON")
	return g.account_db

# closing the database for the accounts and activities
@app.teardown_appcontext
def close_account_db(_error):
	database = g.pop("account_db", None)
	if database is not None:
		database.close()

# checking if the user is logged in and getting the current user
def get_current_user():
	user_id = session.get("user_id")
	if user_id is None:
		return None
	return get_account_db().execute(
		"SELECT id, username FROM users WHERE id = ?", (user_id,)
	).fetchone()

# registering a new account
@app.post("/api/register")
def register_account():
	payload = request.get_json(silent=True)
	if not isinstance(payload, dict):
		return jsonify({"error": "Enter a username and password."}), 400
	username = payload.get("username", "")
	password = payload.get("password", "")
	if not isinstance(username, str) or not re.fullmatch(r"[A-Za-z0-9_]{3,30}", username):
		return jsonify({"error": "Use 3 to 30 letters, numbers, or underscores for your username."}), 400
	if not isinstance(password, str) or not 8 <= len(password) <= 1024:
		return jsonify({"error": "Your password must be between 8 and 1024 characters."}), 400
#saving the new user 
	database = get_account_db()
	try:
		cursor = database.execute(
			"INSERT INTO users (username, password_hash) VALUES (?, ?)",
			(username, generate_password_hash(password)),
		)
		database.commit()
	except sqlite3.IntegrityError: # if the username is already in use
		return jsonify({"error": "That username is already in use."}), 409
#login new user after registration
	session.clear()
	session["user_id"] = cursor.lastrowid
	return jsonify({"username": username}), 201

# logging in to an existing account
@app.post("/api/login")
def login_account():
	payload = request.get_json(silent=True) # getting login info
	if not isinstance(payload, dict):
		return jsonify({"error": "Username or password is incorrect."}), 401
	username = payload.get("username", "")
	password = payload.get("password", "")
	if not isinstance(username, str) or not isinstance(password, str):
		return jsonify({"error": "Username or password is incorrect."}), 401

	user = get_account_db().execute(
		"SELECT id, username, password_hash FROM users WHERE username = ?",
		(username.strip(),),
	).fetchone()
	if user is None or not check_password_hash(user["password_hash"], password):
		return jsonify({"error": "Username or password is incorrect."}), 401
# create the session for the user after successful login
	session.clear()
	session["user_id"] = user["id"]
	return jsonify({"username": user["username"]})

# logging out of the account
@app.post("/api/logout")
def logout_account():
	session.clear()
	return jsonify({"message": "You have been logged out."})

# checking login status 
@app.get("/api/me")
def account_status():
	user = get_current_user()
	if user is None:
		session.clear()
		return jsonify({"logged_in": False})
	return jsonify({"logged_in": True, "username": user["username"]})

# retrieving the activity records for the logged-in user
@app.get("/api/activities")
def list_activities():
	user = get_current_user()
	if user is None:
		return jsonify({"error": "Please log in to view your activity record."}), 401
	records = get_account_db().execute(
		"SELECT id, activity, season, done_at, activity_key FROM activity_records "
		"WHERE user_id = ? ORDER BY id DESC",
		(user["id"],),
	).fetchall()
	return jsonify([dict(record) for record in records])

# recording the completed/ticked activity 
@app.post("/api/activities")
def record_activity():
	user = get_current_user()
	if user is None:
		return jsonify({"error": "Please log in before recording an activity."}), 401
	payload = request.get_json(silent=True)
	if not isinstance(payload, dict):
		return jsonify({"error": "Choose a valid activity."}), 400
	activity = payload.get("activity")
	season = payload.get("season")
	activity_key = payload.get("activity_key")
	if (not isinstance(activity, str) or not activity.strip() or len(activity) > 200
			or not isinstance(season, str) or season not in {"Birak", "Kambarang", "Makuru"}
			or not isinstance(activity_key, str) or not re.fullmatch(r"[A-Za-z0-9_-]{1,80}", activity_key)):
		return jsonify({"error": "Choose a valid activity."}), 400
# check if its already recorded and if not, record the activity
	database = get_account_db()
	existing = database.execute(
		"SELECT id, activity, season, done_at, activity_key FROM activity_records "
		"WHERE user_id = ? AND activity_key = ?",
		(user["id"], activity_key),
	).fetchone()
	if existing is not None:
		return jsonify(dict(existing)), 200
	cursor = database.execute(
		"INSERT INTO activity_records (user_id, activity, season, done_at, activity_key) "
		"VALUES (?, ?, ?, ?, ?)",
		(user["id"], activity.strip(), season, datetime.now(timezone.utc).isoformat(), activity_key),
	)
	database.commit()
	return jsonify({
		"id": cursor.lastrowid,
		"activity": activity.strip(),
		"season": season,
		"done_at": datetime.now(timezone.utc).isoformat(),
		"activity_key": activity_key,
	}), 201

# deleting/removing the activity record from their records/account
@app.delete("/api/activities/<int:record_id>")
def delete_activity(record_id):
	user = get_current_user()
	if user is None:
		return jsonify({"error": "Please log in to update your activity record."}), 401
	database = get_account_db()
	cursor = database.execute(
		"DELETE FROM activity_records WHERE id = ? AND user_id = ?",
		(record_id, user["id"]),
	)
	database.commit()
	if cursor.rowcount == 0:
		return jsonify({"error": "That activity was not found in your record."}), 404
	return jsonify({"message": "Activity removed from your record."})

# sending to browser 
@app.get("/")
def home():
	return send_from_directory(app.root_path, "frontend.html")
# send javascript file to the browser
@app.get("/app.js")
def app_js():
    return send_from_directory(app.root_path, "app.js")
# send data file to the browser
@app.get("/Data/<path:filename>")
def data_file(filename):
	return send_from_directory(os.path.join(app.root_path, "Data"), filename)

# send images to browser 
@app.get("/images/<path:filename>")
def image_file(filename):
	return send_from_directory(os.path.join(app.root_path, "images"), filename)

# saving the feedback from the user to a CSV file
@app.post("/feedback")
def save_feedback():
	payload = request.get_json(silent=True) or {}
	rating = payload.get("rating")
	labels = {
		1: "Very unhappy",
		2: "Unhappy",
		3: "Neutral",
		4: "Happy",
		5: "Very happy",
	}

	if type(rating) is not int or rating not in labels:
		return jsonify({"error": "Choose a rating from 1 to 5."}), 400
# making a feedback record to put to CSV file
	record = {
		"timestamp": datetime.now(timezone.utc).isoformat(),
		"rating": rating,
		"label": labels[rating],
	}
	file_exists = os.path.exists(FEEDBACK_FILE) and os.path.getsize(FEEDBACK_FILE) > 0
	os.makedirs(os.path.dirname(os.path.abspath(FEEDBACK_FILE)), exist_ok=True)

	with open(FEEDBACK_FILE, "a", newline="", encoding="utf-8") as feedback_file:
		writer = csv.DictWriter(feedback_file, fieldnames=record.keys())
		if not file_exists:
			writer.writeheader()
		writer.writerow(record)

	return jsonify({"message": "Thanks for your feedback."}), 201

# starting the application and initializing the database
if __name__ == "__main__":
    init_account_db()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
