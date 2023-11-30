#!/bin/bash
# script that gets the HTTP methods
curl -sl "$1" | grep "Allow:" | cut -d '' -f 2-
