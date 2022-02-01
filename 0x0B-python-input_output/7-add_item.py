#!/usr/bin/python3
"""Adds all arguments to a python list, and them save them to a file"""
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

try:
    list = load("add_item.json")
except Exception:
    list = []

for arg in sys.argv[1:]:
    list.append(arg)
save(list, "add_item.json")
