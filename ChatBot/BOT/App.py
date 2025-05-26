# app.py
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json
from chatbot import get_bot_response  # Import your chatbot logic

app = Flask(__name__, template_folder='Templates')
CORS(app)

@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello from Alia!")

@app.route('/')
def index():
    """
    Render the chatbot UI from /Templates/index.html with CSS styling.
    """
    return render_template('index.html')  # index.html should include <link rel="stylesheet" href="chatbot.css">

@app.route('/get', methods=['GET'])
def get_bot_reply():
    """
    Endpoint for chatbot frontend to send user message and get bot response.
    Expects a 'msg' parameter in the query string.
    """
    user_message = request.args.get('msg', '')
    response = get_bot_response(user_message)
    return response

def lambda_handler(event, context):
    try:
        if event.get("httpMethod") == "GET":
            user_message = event.get("queryStringParameters", {}).get("msg", "")
        else:
            body = json.loads(event.get("body", "{}"))
            user_message = body.get("msg", "")
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid request", "details": str(e)})
        }

    user_message_lower = user_message.lower()
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"response": get_bot_response(user_message_lower)})
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
