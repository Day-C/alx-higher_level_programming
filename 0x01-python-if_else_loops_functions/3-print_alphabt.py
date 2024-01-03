#!/usr/bin/python3
for character in range(26):
    if chr(97 + character) != 'e' and chr(97 + character) != 'q':
        print("{}".format(chr(97 + character)), end="")
