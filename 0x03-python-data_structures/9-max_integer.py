#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    max_num = my_list[0]
    for i in my_list:
        if max_num > i:
            continue
        max_num = i

    return (max_num)
