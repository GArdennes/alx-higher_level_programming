#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

    if type(roman_string) != str or roman_string is None:
        return 0
    else:
        num_list = []
        for c in roman_string:
            if c in roman_dic:
                num_list.append(roman_dic[c])
        prev_int = 0
        for num in num_list:
            if num > prev_int:
                prev_int = num - prev_int
            else:
                prev_int += num
        return prev_int
