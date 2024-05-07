#!/usr/bin/python3
"""
function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    print titles of the first 10 hot posts listed for a given subreddit
    """
    # reddit api endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # set custom User Agent
    headers = {'User-Agent': 'My user Agent 1.0'}

    # send a get request
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for idx in range(10):
                print(children[idx]).get('data').get('title')
        else:
            print("None")
    except Exception:
        print("None")
