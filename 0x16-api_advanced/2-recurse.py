#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and
    returns a list of titles of all hot articles for a given subreddit.
    :param subreddit: The name of the subreddit (str)
    :param hot_list: A list to store the titles of hot articles (list)
    :param after: The pagination
    token for fetching the next page of results (str)
    :return: A list of titles of all hot articles (list),
    or None if the subreddit is invalid or has no hot articles
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:myredditbot:v1.0.0 (by /u/wassola)"
    }
    params = {"after": after, "limit": 100}
    try:
        response = requests.\
            get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            hot_posts = data["data"]["children"]
            if not hot_posts:
                return hot_list if hot_list else None
            hot_list.extend([post["data"]["title"] for post in hot_posts])
            after = data["data"]["after"]
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
