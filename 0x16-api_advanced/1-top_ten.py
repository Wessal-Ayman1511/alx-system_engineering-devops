#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints
    the titles of the first 10 hot posts for a given subreddit.
    :param subreddit: The name of the subreddit (str)
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "windows:myredditbot:v1.0.0 (by /u/yourusername)"
    }
    params = {"limit": 10}
    try:
        response = requests.\
            get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            hot_posts = data["data"]["children"]
            if not hot_posts:
                print(None)
                return

            for post in hot_posts:
                print(post["data"]["title"])
        else:
            print(None)
    except requests.RequestException:
        print(None)
