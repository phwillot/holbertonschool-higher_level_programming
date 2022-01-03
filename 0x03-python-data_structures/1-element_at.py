#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        i = 0
        for element in my_list:
            if i == idx:
                return element
            i += 1
