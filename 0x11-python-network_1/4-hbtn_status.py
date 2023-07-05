#!/usr/bin/python3
'''
 Module to fetch and display the body response of a URL
'''
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)
    body = response.text
    # GET request to the URL and retrieve the response


    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)

    # Print the body response along with the type of the content and the content itself
