#!/usr/bin/python3
"""
Script sends a POST request to URL with email param
"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    email_param = {"email": argv[2]}
    encoded_data = urllib.parse.urlencode(
            email_param).encode("ascii")
    request = urllib.request.Request(
            argv[1],
            encoded_data)

    with urllib.request.urlopen(request) as response:
        response_data = response.read().decode(
                "utf-8")
        print(response_data)
