
import json
#import requests

def endpoint(event, context):
    #current_time = datetime.datetime.now().time()
    print(event.keys())
    
    # respond with a cloudevent
    body = {}
    body['specversion']='1.0'
    body['time']='2018-04-05T03:56:24Z'
    body['id']='XXX-YYY-ZZZ-WWW'
    body['datacontenttype']='Content-type: application/json'

    #headers = {'Content-Type': 'application/cloudevents+json'}
    
    body['data'] = {
        "message": "A commit was made at " + event['repository']['full_name']
    }

    response = json.dumps(body)

    return response
