#!/usr/bin/python3
from sys import argv
import requests


if __name__ == "__main__":
    data = {"email": argv[2]}
    response = requests.post(
            argv[1], json=data)
    print(response.text)
