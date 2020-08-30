# swift_api_client.py

import requests
import sys

SWIFT_SERVER = 'http://192.168.1.20:5000/file_api'


def send_file_to_server(fname):
    # open file for reading
    p = open(fname, 'r')
    contents = p.read()
    response = requests.post(SWIFT_SERVER, data=contents)

    print("Status code: ", response.status_code)
    print("Printing Entire Post Request")
    print(response.text)


def main():
    print('')
    if len(sys.argv) < 2:
        print('Usage:  python swift_api_client.py <json_input>')
        return

    fname = sys.argv[1]

    # open file for reading
    p = open(fname, 'r')
    contents  = p.read()
    response = requests.post(SWIFT_SERVER, json=contents)

    print("Status code: ", response.status_code)
    print("Printing Entire Post Request")
    print(response.text)


if __name__ == '__main__':
    main()
