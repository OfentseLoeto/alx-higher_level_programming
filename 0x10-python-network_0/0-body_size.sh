#!/bin/bash
# This script takes in a URL as argument, sends a request to that URL using curl in silent mode
curl -s -I "$1" | awk '/Content-Length/ {print $2}'
