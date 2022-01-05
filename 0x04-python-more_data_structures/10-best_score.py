#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max = list(a_dictionary.items())[0][1]
        name = ""
        for key, value in a_dictionary.items():
            if a_dictionary[key] > max:
                max = a_dictionary[key]
                name = key
        return name
