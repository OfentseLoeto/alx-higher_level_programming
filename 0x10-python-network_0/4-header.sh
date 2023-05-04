#!/bin/bash
# Sends a GET request with a header X-School-User-Id: 98 and displays the body of the response using curl
curl -s -H "X-School-User-Id: 98" "$1"
