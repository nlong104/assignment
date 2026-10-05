import os

if not os.environ.get("FLASK_SECRET_KEY"):
	raise RuntimeError("Set FLASK_SECRET_KEY in the hosting provider before starting the production app.")

from backend import app, init_account_db

init_account_db()