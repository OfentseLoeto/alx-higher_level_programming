#!/usr/bin/python3
"""This script return the number of subscribers"""
import requests

def number_of_subscribers(subreddit):
    user_agent = ""
    header = {"User-Agent": user_agent}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers=headers)

    if response_status_code == 200:
        try:
            data = response.json()
            subscribers = data["data"]["subscribers"]
            return subscribers
        
        except (KeyError, ValueError):

            return 0
        else:
            return 0
