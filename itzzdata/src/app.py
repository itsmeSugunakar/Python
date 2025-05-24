from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/lambda', methods=['POST'])
def lambda_handler():
    try:
        # Get the JSON payload from the request
        event = request.get_json()
        
        # Simulate Lambda function logic
        response = {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Lambda function executed successfully!",
                "input": event
            })
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({
            "statusCode": 500,
            "body": json.dumps({
                "message": "An error occurred",
                "error": str(e)
            })
        })

def lambda_handler_test():
    # Simulate a test event
    test_event = {
        "Name": "Sugunakar",
        "Org": "Test"
    }
    with app.test_request_context('/lambda', method='POST', json=test_event):
        response = lambda_handler()
        print(response.get_data(as_text=True))


if __name__ == '__main__':
    app.run(debug=True)