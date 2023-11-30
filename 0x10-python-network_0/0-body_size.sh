#!/bin/bash
# script that takes in a URL, sends a request to that URL
curl -sl "$1" | grep 'Content-Length' | awk '{print $2}'
