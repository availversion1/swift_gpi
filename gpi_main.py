# gpi_main.py

from flask import Flask, request, jsonify
import sys

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Smaranath Arunachala!'

COUNT = 1

@app.route('/file_api', methods=['POST'])
def process_json():
    global COUNT

    content = request.get_data()

    COUNT += 1
    print(content)

    return 'Received JSON from client.. #' + str(COUNT)


