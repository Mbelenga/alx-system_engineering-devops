#!/usr/bin/python3
"""
function that queries the Reddit API and returns
the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ retrieve number of subscribers """

    # reddit api endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # set custom User Agent
    headers = {'User-Agent': 'My user Agent 1.0'}

    # send a get request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # check if the request was successful
    if response.status_code == 200:

        # parse json response
        data = response.json().get('data', {})
        sub_count = data.get('subscribers')
        return sub_count
    else:
        return 0
