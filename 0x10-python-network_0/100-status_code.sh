#!/bin/bash
# script sends a request to the URL passed as an argument using curl in silent mode and displays only the status code
curl -s -o /div/null -w "%{http_code}" "$1"
