#!/usr/bin/python3
"""
Sends a request to the URL and displays the value
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    request = urllib.request.Request(argv[1])
    with urllib.request.urlopen(request) as response:
        x_request_id = response.getheader(
                "X-Request-Id")
        print(x_request_id)
