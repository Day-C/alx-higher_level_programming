#!/usr/bin/python3
def  max-integer(my_list=[]):
    if my_list == None:
        return (None)
    max = 0
    for i in my_list:
        if max > i:
            continue
        max = i

    return (max)
