"""Database access functions."""

from functools import wraps
import sqlite3

DBNAME = "clicks.db"


def with_db(func):
    """Call function with sqlite3 cursor. Close the database connection after."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            con = sqlite3.connect(DBNAME)
            cur = con.cursor()
            res = func(cur, *args, **kwargs)
            con.commit()
            return res
        finally:
            con.close()

    return wrapper


@with_db
def get_clicks(cur=None) -> int:
    """Get the number of clicks from the database."""
    clicks_res = cur.execute("SELECT num_clicks FROM clicks LIMIT 1")
    row = clicks_res.fetchone()
    return row[0]


@with_db
def save_click(cur=None) -> int:
    """Save the click to the database."""
    # get the current number of clicks from DB
    clicks_res = cur.execute("SELECT num_clicks FROM clicks LIMIT 1")
    row = clicks_res.fetchone()

    num_clicks = row[0]
    num_clicks += 1

    cur.execute("UPDATE clicks SET num_clicks = ?", (num_clicks,))
    return num_clicks
