#!/bin/bash
# Script takes a URL as an argument, sends a GET request to that URL with a custom header using curl in silent mode
curl -s -H "X-School-User-Id: 98" "$1"
