#!/usr/bin/python3
'''
 Module to retrieve the user ID using GitHub API.
'''
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    access_token = sys.argv[2]

    url = f"https://api.github.com/user"

    headers = {
            "Authorization": f"Basic {username}:{access_token}",
            "Accept": "application/vnd.github.v3+json"
            }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response,json()
        user_id = user_data['id']
        print("User Id:", user_id)

    else:
        print("Failed to retrive user ID. Status code:", response.status_code)


