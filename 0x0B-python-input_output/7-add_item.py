#!/usr/bin/python3
"""
Task 7
"""


import sys
import os


save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__(
        '6-load_from_json_file.py').load_from_json_file


my_list = []
if os.path.exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")

my_list.extend(sys.argv[1:])
save_to_json_file(my_list,  "add_item.json")
