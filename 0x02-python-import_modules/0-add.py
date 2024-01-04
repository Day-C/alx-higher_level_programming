#!/usr/bin/python3
adding = __import__('add_0').add
if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, adding(a, b)))
