#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    n = 0
    for i in my_list:
        if n == idx:
            my_list.remove(i)
        n += 1
    return my_list
