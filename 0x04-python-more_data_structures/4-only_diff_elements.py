#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    uniq = []
    for element in set_1:
        if element in set_1 and element not in set_2:
            uniq.append(element)
    for element in set_2:
        if element not in set_1 and element in set_2:
            uniq.append(element)
    return uniq
