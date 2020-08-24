# gpi_main.py

from flask import Flask, request, jsonify
import sys

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Smaranath Arunachala!'


@app.route('/swift_api', methods=['POST'])
def process_json():
    content = request.get_json()

    print(content)
    return 'This function will process JSON!'


