#!/usr/bin/python3
'''
Module to fetch and display the body response of a URL.
'''
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get('https://alx-intranet.hbtn.io/status')
    body = response.text


    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
