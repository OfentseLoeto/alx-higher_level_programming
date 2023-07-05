#!/usr/bin/python3
'''
Script that fetches https://alx-intranet.hbtn.io/status
'''
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read()
    # Fetches the URL using urlopen from urllib.request

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))
    # Prints the body response along with the type of the content,
    # the content itself, and the UTF-8 decoded content
