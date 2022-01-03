#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        for j in element:
            print("{:d}".format(j), end=" ")
        print()
