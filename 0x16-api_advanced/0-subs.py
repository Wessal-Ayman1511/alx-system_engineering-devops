#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests
headers = {'User_Agent': 'MyAPI/0.0.1', 'Authorization': 'bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzIzNjQyMjUyLjE3MTkwNiwiaWF0IjoxNzIzNTU1ODUyLjE3MTkwNiwianRpIjoiS1YwSjNyenNXdEZyUWEza3IwVzZyOWI2VFhUcnBnIiwiY2lkIjoiVzFUY1h5aEpUaXR6RDd4SWJxZXF3USIsImxpZCI6InQyXzE2a3VnN2tkaGQiLCJhaWQiOiJ0Ml8xNmt1ZzdrZGhkIiwibGNhIjoxNzIzNTUwNzQ5MjA4LCJzY3AiOiJlSnlLVnRKU2lnVUVBQURfX3dOekFTYyIsImZsbyI6OX0.ERKFUjV4GigxOhcJn-KvMzNqEW0bxdfc6FANdfeUowgFoaniNKkGg9kTwgQIdU_EloWOnLd7HDGA1ZytqefKd0GUXPJRrxmlwLmmyGQxuxgY7HSV9QD6CPXAUmw6bAPkJt_O748K5T72D0ZGH6EULv9fwWPLVSj8WFQ40d89u6sQ0vRCbHVQ4PYxiFConSqJ9zx00AttEIuZISHcc-vuXJe2mAmnHdZXzcoYV8iWE0f2DNgfT9K6wEFrKOW03XMWwcNDrksMkqBLsw6Jg5VKEhTBdci39C3zAwz37Pp1NrIZbaOJRdQMV8nAu9X2kXSJ07gCkO6eoWGqop0jtEhmkQ'}



def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://oauth.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
