# app.py
from flask import Flask, jsonify
from flask_cors import CORS # Import CORS for handling Cross-Origin Resource Sharing

app = Flask(__name__)
# Enable CORS for all origins. In a production environment,
# you should restrict this to your specific frontend domain.
CORS(app)

@app.route('/hello', methods=['GET'])
def hello_world():
    """
    A simple endpoint that returns a JSON message.
    This will be the endpoint that your frontend calls.
    """
    return jsonify(message="Hello from Flask Backend!")

@app.route('/')
def index():
    """
    A basic root endpoint. Not directly used by the SPA in this setup,
    but good for a quick check if the Flask app is running.
    """
    return "Flask app is running!"

if __name__ == '__main__':
    # When running locally, the app will be accessible at http://127.0.0.1:5000/
    # For deployment, this will be handled by your deployment environment (e.g., Gunicorn, uWSGI)
    # and integrated with API Gateway.
    app.run(debug=True, host='0.0.0.0', port=5000)
