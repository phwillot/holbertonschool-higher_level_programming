#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        i = 0
        for item in my_list:
            if i == idx:
                my_list[i] = element
            i += 1
        return my_list
