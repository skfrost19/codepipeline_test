import json
import requests
from dateutil import parser
from datetime import datetime

def lambda_handler(event, context):
    # Extract name from the request body
    body = json.loads(event.get("body", "{}"))
    name = body.get("name", "World")

    # Fetch current date-time and parse it using dateutil
    current_time = datetime.now().isoformat()
    parsed_time = parser.parse(current_time)

    # Make a dummy HTTP request (e.g., to a public API)
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        api_data = response.json()
    except Exception as e:
        api_data = {"error": str(e)}

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Hey {name}!",
            "current_time": parsed_time.strftime("%Y-%m-%d %H:%M:%S"),
            "api_data": api_data
        })
    }
