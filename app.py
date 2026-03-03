from datetime import date    # ✅ ဒီလို uncomment လုပ်ထားရမယ်
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    start = date(2022, 12, 14)  # anniversary date
    today = date.today()

    delta = today - start
    days = delta.days
    years = days // 365
    months = (days % 365) // 30
    rem_days = (days % 365) % 30

    return render_template("index.html", years=years, months=months, days=rem_days)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render gives PORT env variable
    app.run(host="0.0.0.0", port=port, debug=True)