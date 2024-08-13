#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "PostmanRuntime/7.41.0",
        "Authorization": "bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzIzNjM3NjA5LjMyMDg0OSwiaWF0IjoxNzIzNTUxMjA5LjMyMDg0OCwianRpIjoicHVnVGRWcmYwZndFbG1YM0kxelUxVWNzbUcwbWRBIiwiY2lkIjoiVzFUY1h5aEpUaXR6RDd4SWJxZXF3USIsImxpZCI6InQyXzE2a3VnN2tkaGQiLCJhaWQiOiJ0Ml8xNmt1ZzdrZGhkIiwibGNhIjoxNzIzNTUwNzQ5MjA4LCJzY3AiOiJlSnlLVnRKU2lnVUVBQURfX3dOekFTYyIsImZsbyI6OX0.FjrtJKlXBhWJb9HcbIjskA06QBJSKFuzZD6PBstW2joznSBkA1dUn6Y4z5slFdBImiHpgt5LxOjJ2oFsrA-V-VNSII7gJDfyo1WgMrH2OSzp-pGeg1MA9AT60d1f3FSU_Fiv0kOV6-fNVthyB0tAtzgPPHi_lX5Z7_8KWMiNAEKBT4ncGzDOl9bhHa4Cld421D-M1wA9x0BhRsUOIH-LNxQFmtElppqiw0427PiYyMRPG7eg4MxQSCqHm_xUwwlKlcQeNDI3g7dWuJhldTdTsWlpca9jw--vGIDoSETcF38IOFZCK1y2pLXQ7JJ3Uzu36hpcuT3cU1TZy98qan6mig"
        
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
