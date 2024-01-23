#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    value = 0
    try:
        value = fct(args)
    except ZeroDivisionError:
        sys.stderr.write("division by zero\n")
        return (None)
    except IndexError:
        sys.stderr.write("index out of range\n")
        return (None)
    except TypeError:
        sys.stderr.write("wrong type\n")
    return (value)
