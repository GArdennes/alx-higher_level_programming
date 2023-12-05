#!/usr/bin/python3
"""
Script that sends a request to a URL
"""
import urllib.request
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    request = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(
               request) as response:
            response_data = response.read(
                    ).decode("utf-8")
            print(response_data)
    except urllib.error.HTTPError as e:
        print("Error: {}".format(e.code))
