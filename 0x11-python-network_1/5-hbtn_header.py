#!/usr/bin/python3
"""
Sends a request to a URL and displays the X-Request-Id
"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get(argv[1])
    x_request_id = response.headers.get(
            "X-Request-Id")
    print(x_request_id)
