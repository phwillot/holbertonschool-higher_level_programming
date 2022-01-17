#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        fct(*args)
        return fct(*args)
    except (ZeroDivisionError, IndexError) as e:
        sys.stderr.write("Exception: ")
        sys.stderr.write(str(e))
        sys.stderr.write("\n")
        return None
