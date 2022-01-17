#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for elt in range(0, x):
            print("{:d}".format(my_list[elt]), end="")
        return x
    except IndexError:
        return elt
    finally:
        print()
