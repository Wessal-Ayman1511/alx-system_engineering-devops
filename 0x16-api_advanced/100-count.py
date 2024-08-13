#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Recursively queries the Reddit API to
    parse titles of all hot articles
    and counts the occurrences of given keywords.
    :param subreddit: The name of the subreddit (str)
    :param word_list: A list of keywords to count in the titles (list)
    :param word_count: A dictionary to keep track of word counts (dict)
    :param after:
    The pagination token for fetching the next page of results (str)
    """
    # Base URL for the Reddit API request
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "windows:myredditbot:v1.0.0 (by /u/yourusername)"
    }
    params = {"after": after, "limit": 100}

    try:
        # Making the API request
        response = requests\
            .get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            hot_posts = data["data"]["children"]
            after = data["data"]["after"]

            # Initialize word_count dictionary if it's the first call
            if not word_count:
                word_count = {word.lower(): 0 for word in word_list}

            # Count keywords in each title
            for post in hot_posts:
                title_words = post["data"]["title"].lower().split()
                for word in title_words:
                    if word in word_count:
                        word_count[word] += title_words.count(word)
            # Recursive call if there's more data (pagination)
            if after:
                return count_words(subreddit, word_list, word_count, after)
            else:
                # Sort the dictionary and print results
                sorted_words = sorted(
                    word_count.items(), key=lambda item: (-item[1], item[0])
                    )
                for word, count in sorted_words:
                    if count > 0:
                        print(f"{word}: {count}")
        else:
            return None
    except requests.RequestException:
        return None
