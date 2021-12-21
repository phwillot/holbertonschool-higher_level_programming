#!/usr/bin/python3
def uppercase(str):
    for element in str:
        if ord(element) >= 97 and ord(element) <= 122:
            element = chr(ord(element) - 32)
        print("{:s}".format(element), end = "")
    print()
