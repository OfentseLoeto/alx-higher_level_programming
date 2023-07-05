#!/usr/bin/python3
'''
Module to send a POST request with an email parameter and display the response body.
'''
import sys
import urllib.request
import urllib.parse

if __name__ == "__main___":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encoding email parameters
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Create a POST reaquest
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(request) as response:
        body = response.read().encode('utf-8')

        print("Your email is:", body)
