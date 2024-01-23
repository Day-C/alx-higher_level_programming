#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n = []
    lon = 0
    if len(my_list_1) > len(my_list_2):
        lon = len(my_list_1)
    elif len(my_list_1) < len(my_list_2):
        lon = len(my_list_2)
    else:
        lon = len(my_list_1)
    for i in range(lon):
        try:
            n.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            n.append(0)
        except IndexError:
            print("out of range")
            n.append(0)
        except TypeError:
            print("wrong type")
            n.append(0)
        finally:
            pass

    return (n)
