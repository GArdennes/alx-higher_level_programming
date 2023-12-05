#!/usr/bin/python3
"""
Sends a POST request to a URL with letter as param
"""
import requests
from sys import argv


if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]
    pay_load = {"q": letter}
    url = requests.post(
            "http://0.0.0.0:5000/search_user",
            data=pay_load)
    try:
        response = url.json()
        if response == {}:
            print("No result")
        else:
            print("[{}]{}".format(
                response.get("id"),
                response.get("name")))
    except Exception:
        print("Not a valid JSON")
