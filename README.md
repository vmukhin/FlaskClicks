# Clicks

This is the absolutely most basic Flask app that shows a single button and records the
number of times the button has been clicked in a sqlite database.

There are many, many different ways to improve and extend this app, which is the entire
point of web development.

## How to run

1. Create a Python virtual environment and install Flask:

   ```bash
   python -m virtualenv venv
   . venv/bin/activate
   pip install Flask
   ```

2. Initialize the database, create the table and seed the initial data:

   ```bash
   $ sqlite3 clicks.db 
   sqlite> CREATE TABLE clicks (num_clicks INTEGER);
   sqlite> INSERT INTO clicks VALUES (0);
   sqlite> .exit
   $
   ```

3. Run the Flask app:

   ```bash
   flask --app clicks run
   ```

4. Now visit http://127.0.0.1:5000 in a browser to see the app.
