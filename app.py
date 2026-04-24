from datetime import date
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)


@app.route("/")
def home():
    start = date(2023, 1, 3)
    today = date.today()

    delta = today - start
    days = delta.days
    years = days // 365
    months = (days % 365) // 30
    rem_days = (days % 365) % 30

    return render_template("index.html",
                           years=years,
                           months=months,
                           days=rem_days)


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            return redirect(url_for("home"))
        else:
            return "Wrong username or password"

    return render_template("login.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)