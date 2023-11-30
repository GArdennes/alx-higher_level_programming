#!/bin/bash
# script that gets the HTTP methods
curl -sI "$1" | grep "Allow" | cut -d '' -f 2-
