#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argument = len(sys.argv) - 1
    counter = 0
    if argument == 0:
        print("0 arguments.")
    elif argument == 1:
        print("1 argument:")
        for arg in sys.argv:
            if counter != 0:
                print("{:d}: {:s}".format(counter, arg))
            counter += 1
    else:
        print("{:d} arguments:".format(argument))
        for arg in sys.argv:
            if counter != 0:
                print("{:d}: {:s}".format(counter, arg))
            counter += 1
