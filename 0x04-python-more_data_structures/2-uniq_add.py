#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    sum = 0
    for number in my_list:
        if number not in uniq:
            sum = sum + number
            uniq.append(number)
    return sum
