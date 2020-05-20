#!/usr/bin/env python3


from flask import Flask
from flask import request

import os
import json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def trans():
    ce = request.get_json()
    print(ce.keys())
    
    # respond with a cloudevent
    headers = {}
    headers['ce-specversion']='1.0'
    headers['ce-time']='2018-04-05T03:56:24Z'
    headers['ce-id']='XXX-YYY-ZZZ-WWW'
    headers['content-type']='application/json'
    headers['ce-type']='com.triggermesh.transform'
    headers['ce-source']='whatever'
    
    body = {}
    # FOR GITUHB
    #body = {
    #    "message": "A commit was made at " + ce['repository']['full_name']
    #}

    # FOR SQS
    body = {
        "message": "AWS SQS says " + ce['body']
    }

    print(body)
    response = app.response_class(
            response=json.dumps(body),
            headers=headers,
            status=200,
            mimetype='application/json'
    )

    return response 

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
