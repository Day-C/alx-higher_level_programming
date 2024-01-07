#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        j = j+1
        print("{}{}".format(i, j), end=", ")
        if j == 9:
            i = i + 2
