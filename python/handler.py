
import json
import datetime


def endpoint(event, context):
    #current_time = datetime.datetime.now().time()
    print(json.loads(event))
    body = {
        "message": "Hello from repo " + event['body']['repository']['full_name']
    }

    response = json.dumps(body)

    return response
