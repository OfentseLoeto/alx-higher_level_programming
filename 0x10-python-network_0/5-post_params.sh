#!/bin/bash
# Script takes a URL as an argument, sends a GET request to that URL with a custom header using curl in silent mode
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
