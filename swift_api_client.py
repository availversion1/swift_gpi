# swift_api_client.py

import requests
import sys

SWIFT_SERVER = 'http://192.168.29.12:5000/swift_api'

def main():
    print('')
    if len(sys.argv) < 2:
        print('Usage:  python swift_api_client.py <json_input>')
        return

    fname = sys.argv[1]

    #open file for reading
    p = open(fname, 'r')
    contents  = p.read()
    response = requests.post(SWIFT_SERVER, json=contents)

    print("Status code: ", response.status_code)
    print("Printing Entire Post Request")
    print(response.text)


if __name__ == '__main__':
    main()
