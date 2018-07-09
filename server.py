from flask import Flask, jsonify

import csv_to_json

app = Flask(__name__)

@app.route('/')
def serve_index():
  return app.send_static_file('index.html')

@app.route('/network')
def get_network_data():
  return jsonify(csv_to_json.processData())