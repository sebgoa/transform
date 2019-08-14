
import json
import datetime


def endpoint(event, context):
    current_time = datetime.datetime.now().time()
    body = {
        "message": "Hello, this is wednesday " + str(current_time)
    }

    response = json.dumps(body)

    return response
