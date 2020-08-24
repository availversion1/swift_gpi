# gpi_main.py

from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Smaranath Arunachala!'


@app.route('/swift_api')
def process_json():
    return 'This function will process JSON!'


@app.route('/shutdown')
def shut_down():
    sys.exit(0)