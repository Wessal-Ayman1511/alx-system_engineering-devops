#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "PostmanRuntime/7.41.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
