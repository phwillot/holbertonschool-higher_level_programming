#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    dict = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    sum = 0
    for i in range(len(roman_string)):
        if i != len(roman_string) - 1 \
                and dict[roman_string[i]] < dict[roman_string[i + 1]]:
            sum += dict[roman_string[i]] * -1
        else:
            sum += dict[roman_string[i]]
    return sum
