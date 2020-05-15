
import json
import datetime


def endpoint(event, context):
    #current_time = datetime.datetime.now().time()
    print(event.keys())
    body = {
        "message": "A commit was made at " + event['repository']['full_name']
    }

    response = json.dumps(body)

    return response
