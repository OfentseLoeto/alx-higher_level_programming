#!/bin/bash
# This script takes a URL as an argument, sends a GET request to that URL using curl in silent mode
response_code=$(curl -s -o /dev/null -w "%{http_code}" "$1") [[ $response_code == "200" ]] && curl -s "$1" || echo "Response code: $response_code"
