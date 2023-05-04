#!/bin/bash

# Sends a JSON POST request to a URL and displays the response body

if [ $# -ne 2 ]; then
  echo "Usage: $0 url filename"
  exit 1
fi

url=$1
filename=$2

# Read the contents of the file into a variable
data=$(cat "$filename")

# Send the POST request with the data in the body, and display the response body
curl -s -X POST -H "Content-Type: application/json" -d "$data" "$url"

