#!/usr/bin/python3
"""
Fetch URL with urllib
"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request(
            "https://alx-intranet.hbtn.io/status"
            )
    with urllib.request.urlopen(
            request
            ) as response:
        html_content = response.read()
        print("Body response.")
        print("\t- type: {}".format(
            type(html_content)))
        print("\t- content: {}".format(
            html_content))
        print("\t- utf8 content: {}".format(
            html_content.decode("utf-8")))
