#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list = my_list[:]
        i = 0
        for item in new_list:
            if i == idx:
                new_list[i] = element
            i += 1
        return new_list
