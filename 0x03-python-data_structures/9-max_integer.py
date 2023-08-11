#!/usr/bin/python3
def max_integer(my_list=[]):
    new_list = my_list[:]
    new_list.sort()
    return new_list[-1] if new_list else None
