"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
input_string = raw_input(">")
tokens = input_string.split(" ")
if tokens[0] == "+":
    print add(int(tokens[1]), int(tokens[2]))
