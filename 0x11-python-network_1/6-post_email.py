#!/usr/bin/python3
"""
Script to post and email
"""
from sys import argv
import requests


if __name__ == "__main__":
    json = {"email": argv[2]}
    response = requests.post(
            argv[1], data=json)
    print(response.text)
