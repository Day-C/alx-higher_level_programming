#!/usr/bin/python3
def safe_print_division(a, b):
    n = 0
    try:
        n = a / b
        print("Inside result: {}".format(n))
    except ZeroDivisionError:
        print("Inside result: None")
        return (None)
    return (n)
