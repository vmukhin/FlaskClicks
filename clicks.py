"""Clicks counter"""

from json import dumps

from flask import Flask, render_template

from clicks_db import get_clicks, save_click

app = Flask(__name__)


@app.route("/")
def index():
    """Render the page"""
    num_clicks = get_clicks()
    return render_template("./index.html", num_clicks=num_clicks)


@app.route("/saveclick", methods=["POST"])
def save():
    """Save the click"""
    num_clicks = save_click()
    return dumps({"clicks": num_clicks})
