# coding: utf-8
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/test", methods=["POST"])
def post_test_secret():
    print(request.form["secret"])
    return jsonify({
        "status": "OK",
        "secret": request.form["secret"]
    })


if __name__ == "__main__":
    app.run()
