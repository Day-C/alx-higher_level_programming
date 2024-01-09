#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum_ = 0
    argv = sys.argv
    if len(argv) == 1:
        pass
    else:
        for i in range(1, len(argv)):
            n = int(argv[i])
            sum_ += n
    print("{}".format(sum_))
