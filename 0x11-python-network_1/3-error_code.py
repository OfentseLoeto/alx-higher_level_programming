#!/usr/bin/python3
'''
Module to fetch and display the body response of a URL, handling HTTP errors.
'''
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen('http://0.0.0.0:5000') as response:
            body = response.read().decode('utf-8')
            print(body)

    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
        print("Error code:", e.read)
        
        #  Print the HTTP status code in case of an error

