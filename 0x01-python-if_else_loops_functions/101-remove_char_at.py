#!/usr/bin/python
def remove_char_at(str, n):
    
    if n >= 0 and n < len(str) + 1:
        str = str[:n] + str[n+1:]
        return (str)
    else:
        return (str)
