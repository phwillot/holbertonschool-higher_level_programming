#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for elt, key in new.items():
        new[elt] *= 2
    return new
