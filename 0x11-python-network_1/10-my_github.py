#!/usr/bin/python3
"""
Script uses GitHub credentials to access info
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(
            argv[1], argv[2])
    request = requests.get(
            "https://api.github.com/user",
            auth=auth)
    print(request.json().get("id"))
