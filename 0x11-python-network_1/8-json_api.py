#!/usr/bin/python3
'''
 Module to send a POST request with a letter parameter and display the id and name from the response.
'''
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': letter}
    response = requests.post(url, data=data)

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
        else:
            print("No results")
    except ValueError:
        print("Not a valid JSON")
