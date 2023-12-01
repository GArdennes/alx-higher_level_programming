#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    if list_of_integers is None or not list_of_integers:
        return None

    start = 0
    end = len(list_of_integers) - 1
    peak = None
    done = False

    while not done:
        if start <= end:
            mid = (start + end) // 2

            if (mid == 0 or list_of_integers[mid] > list_of_integers[mid - 1]) and \
               (mid == end or list_of_integers[mid] > list_of_integers[mid + 1]):
                peak = list_of_integers[mid]
                done = True
            else:
                if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
                    end = mid - 1
                else:
                    start = mid + 1
        else:
            done = True

    return peak
