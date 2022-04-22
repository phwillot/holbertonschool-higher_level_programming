#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL
and displays the body of the response"""
import sys
from urllib import error, request

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            data = response.read().decode('utf-8')
            print(data)
    except error.HTTPError as err:
        print("Error code: {}".format(err.getcode()))
