#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for i in my_list:
        if i == 0:
            result.append(True)
            continue
        if 2 % i == 0:
            result.append(True)
        result.append(False)
    return (result)
