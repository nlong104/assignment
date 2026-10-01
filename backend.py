import csv, json, os # modules built into Python (no install needed)
from datetime import datetime, timezone
from flask import Flask, jsonify, request, send_from_directory # tools taken from the Flask library
app = Flask(__name__) # create the web application

# feedback for the website 
FEEDBACK_FILE = os.path.join(app.root_path, "feedback.csv")


@app.get("/")
def home():
	return send_from_directory(app.root_path, "frontend.html")


@app.get("/Data/<path:filename>")
def data_file(filename):
	return send_from_directory(os.path.join(app.root_path, "Data"), filename)


@app.get("/images/<path:filename>")
def image_file(filename):
	return send_from_directory(os.path.join(app.root_path, "images"), filename)


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

	record = {
		"timestamp": datetime.now(timezone.utc).isoformat(),
		"rating": rating,
		"label": labels[rating],
	}
	file_exists = os.path.exists(FEEDBACK_FILE) and os.path.getsize(FEEDBACK_FILE) > 0

	with open(FEEDBACK_FILE, "a", newline="", encoding="utf-8") as feedback_file:
		writer = csv.DictWriter(feedback_file, fieldnames=record.keys())
		if not file_exists:
			writer.writeheader()
		writer.writerow(record)

	return jsonify({"message": "Thanks for your feedback."}), 201


if __name__ == "__main__":
	app.run(port=8000)

