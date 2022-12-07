#!/usr/bin/python3
def no_c(my_string):
    n = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            print("{}".format(char), end="")
    return n
