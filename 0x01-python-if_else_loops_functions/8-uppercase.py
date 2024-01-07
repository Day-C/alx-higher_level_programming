#!/usr/bin/python3
def uppercase(str):
    new_str = []
    for i in range(len(str)):
        if ord(str[i] in range(97, 123)):
            new_str[i] = chr(ord(str[i] - 32))
        else:
            new_str[i] = str[i]
        print("{}".format(new_str[i]), end="")
    print("")
