#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type: {}".format(type(r.content.decode('utf-8'))))
    print("\t- content: {}".format(r.content.decode('utf-8')))
