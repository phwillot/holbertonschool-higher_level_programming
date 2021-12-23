#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys

    count = 0

    if len(sys.argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = ["+", "-", "*", "/"]
    for operator in operators:
        if sys.argv[2] == operator:
            count += 1
    if count == 0:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[3])

        if sys.argv[2] == "+":
            print("{} + {} = {}".format(num1, num2, calc.add(num1, num2)))
        if sys.argv[2] == "-":
            print("{} - {} = {}".format(num1, num2, calc.sub(num1, num2)))
        if sys.argv[2] == "*":
            print("{} * {} = {}".format(num1, num2, calc.mul(num1, num2)))
        if sys.argv[2] == "/":
            print("{} / {} = {}".format(num1, num2, calc.div(num1, num2)))
