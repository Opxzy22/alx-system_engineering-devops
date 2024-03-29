#!/usr/bin/python3
"""a function that queries the Reddit API and return
s the number of subscribers (not active users, total subscribers) fo
r a given subreddit. If an invalid subreddit is given
, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
