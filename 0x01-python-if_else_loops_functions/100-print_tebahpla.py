#!/usr/bin/python3
for letters in range(122, 96, -2):
    print("{:s}{:s}".format(chr(letters), chr(letters - 33)), end= "")

