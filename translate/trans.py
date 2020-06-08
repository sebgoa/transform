#!/usr/bin/env python3

from flask import Flask
from flask import request
from googletrans import Translator

import os
import json

app = Flask(__name__)
translator = Translator()

@app.route('/', methods=['POST', 'GET'])
def trans():
    ce = request.get_json()
    print(ce.keys())
    
    # respond with a cloudevent
    headers = {}
    headers['ce-specversion']='1.0'
    headers['ce-time']='2020-06-05T03:56:24Z'
    headers['ce-id']='XXX-YYY-ZZZ-WWW'
    headers['content-type']='application/json'
    headers['ce-type']='com.triggermesh.translate'
    headers['ce-source']='google-translate'
    
    body = {}
    # FOR SLACK SOURCE
    result = translator.translate(ce['text'], dest='es')
    print(result.text)
    body = {
        "channel": "tmspanish",
        "text": ce['user_id'] + " says: " + result.text
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
