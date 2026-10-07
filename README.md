# assignment



# testing the application 
    # javascript tests
    To complete tests 1-5, which are javascript tests, you are to open test.html in finder/file explorer by double clicking on the file. This should open test.html into a browser, and it should open as a blank page. To determine whether the app passes or fails tests 1-5, you are to right-click anywhere on the blank page that has just opened and go to "inspect element", then go to the console tab in the panel that has opened. There will be five lines that will either say pass or fail, showing the results of the first 1-5 tests.

    # python tests
    To complete tests 6-10, which are python tests, make sure that the terminal is in the Data folder (The folder that test_data.py is in) and run python3 test_data.py (on Mac) or py test_data.py (on Windows). It will return five lines that are either pass or fail, showing the results for these automated tests.


# Deploying the web application

The application can be deployed as a Flask web service (On Railway) so visitors can use it without downloading the code.

1. Push this project to a GitHub repository and connect that repository to a new web service.
2. Set the build command to `pip install -r requirements.txt`.
3. Set the start command to `gunicorn --workers 1 --bind 0.0.0.0:$PORT wsgi:app`.
4. Add a persistent disk mounted at `/var/data`. Set `ACCOUNT_DB` to `/var/data/accounts.sqlite3` and `FEEDBACK_FILE` to `/var/data/feedback.csv` so accounts and feedback survive deployments.
5. Set `FLASK_SECRET_KEY` to a generated secret and `FLASK_COOKIE_SECURE` to `1`. Do not commit these secret values to GitHub.
6. Deploy the service. The hosting provider will give it a public URL.
the URL given is: https://assignment-production-e415.up.railway.app

Keep the service to one running instance while using SQLite. If the application needs multiple instances, move the account and feedback storage to a managed database such as PostgreSQL.
