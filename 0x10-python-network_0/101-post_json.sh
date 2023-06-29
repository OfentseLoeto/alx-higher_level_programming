#!/bin/bash
# Script that sends a JSON POST request to a URL passed as the first argument
curl -s -X POST -H "Content_Type: application/Json" -d "@$2" "$1"
