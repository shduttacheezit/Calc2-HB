"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here

while True:
    input_string = raw_input(">")
    tokens = input_string.split(" ")
    if tokens[0] == "q":
        break
    try:
        i = len(tokens)
        num1 = int(tokens[1])
        num2 = int(tokens[-1])
        if tokens[0] == "+":
            print add(num1, num2)
        elif tokens[0] == "-":
            print subtract(num1, num2)
        elif tokens[0] == "*":
            print multiply(num1, num2)
        elif tokens[0] == "/":
            print divide(num1, float(num2))
        elif tokens[0] == "square":
            print square(num1)
        elif tokens[0] == "cube":
            print cube(num1)
        elif tokens[0] == "pow":
            print power(num1, num2)
        elif tokens[0] == "mod":
            print mod(num1, num2)
        else:
            print "I don't understand"
    except:
        print "I don't understand"