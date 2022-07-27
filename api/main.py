#!/usr/bin/env python3



import json
from flask import Flask, jsonify,request
locations = []

app = Flask(__name__)
@app.route('/')
def index():
    first_name = request.args.get('first_name')
    print(first_name)
    
    print(record)
    print(record["key"])
    print(type(record["key"]))
    print(type(record["arr"]))
    return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})
            

@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    record = json.loads(request.data)
    locations.append(record)
    return ('suceuss')
    
@app.route('/get_map_locations', methods=['GET'])
def get_map_locations():
    return jsonify(locations)
   

app.run()