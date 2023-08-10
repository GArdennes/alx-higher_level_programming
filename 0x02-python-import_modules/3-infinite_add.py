#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 0
    args = sys.argv[1:]
    for i in args:
        count += int(i)
    print("{}".format(count))
