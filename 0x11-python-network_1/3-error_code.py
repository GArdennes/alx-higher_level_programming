#!/usr/bin/python3
"""
Script that sends a request to a URL
"""
import urllib.request
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    try:
        request = urllib.request.Request(argv[1])
        with urllib.request.urlopen(
                argv[1]) as response:
            response_data = response.read(
                    ).decode("ascii")
            print(response_data)
    except urllib.error.HTTPError as e:
        print("Error: {}".format(e.code))
