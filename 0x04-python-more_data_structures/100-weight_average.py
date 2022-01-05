#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    sum = 0
    for element in my_list:
        average += element[0] * element[1]
        sum += element[1]
    average /= sum
    return average
