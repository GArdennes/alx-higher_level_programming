#!/bin/bash
# script that sends a JSON POST request to a URL
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
