#!/bin/bash
# This script takes a URL as an argument and displays all HTTP methods the server will accept
curl -s -I -X OPTIONS "$1" | awk '/Allow/ {print substr($0, index($0, $2))}'
