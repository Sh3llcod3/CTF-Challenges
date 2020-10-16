#!/usr/bin/env python3

from flask import Flask, request, render_template
from secrets import compare_digest

app = Flask(__name__, static_folder="static")

challenge_flag = "elite{B1g_Sm0ke's_Ord3r}" # Set your flag here
challenge_answer_encoded = "NDQ1NQ=="

@app.route('/', methods=["GET"])
def index_page():
    return render_template("index.html")

@app.route('/attempt_answer/<answer>', methods=["POST"])
def verify_answer(answer):
    if compare_digest(answer, challenge_answer_encoded):
        return challenge_flag
    else:
        abort(403)

if __name__ == "__main__":
    app.run(debug=False)