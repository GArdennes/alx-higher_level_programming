#!/usr/bin/python3
"""
Finds a peak integer in a lsit of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Implements the modified binary sort algorithm
    Returns the peak number or none
    """
    if list_of_integers is None or not list_of_integers:
        return None
    start = 0
    end = len(list_of_integers)-1
    peak = None
    done = False
    while not done:
        if start <= end:
            mid = (start+end)//2
            if mid == start or\
                    list_of_integers[mid] > list_of_integers[mid-1] and\
                    if mid == end or\
                    list_of_integers[mid] > list_of_integers[mid + 1]:
                peak = list_of_integers[mid]
                done = True
            else:
                if list_of_integers[mid] < list_of_integers[mid - 1]:
                    end = mid - 1
                else:
                    start = mid + 1
        else:
            done = True
    return peak
