#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        for i in (my_list):
            if n < x:
                n += 1
                print("{}".format(i), end = "")
        print()
    except:
        return (0)
    return (n)
