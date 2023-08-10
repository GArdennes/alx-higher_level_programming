#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    args = sys.argv[1:]
    if (len(args) == 0):
        print("{} arguments.".format(len(args)))
    elif (len(args) == 1):
        print("{} argument:".format(len(args)))
        print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments:".format(len(args)))
        while (i < len(args)):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
