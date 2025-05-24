# app.py
from flask import Flask, render_template, request, jsonify
from BOT.chatbot import get_bot_response  # optional if chatbot logic is separated

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response_route():
    user_input = request.args.get("msg")
    return get_bot_response(user_input)

if __name__ == "__main__":
    app.run(debug=True)