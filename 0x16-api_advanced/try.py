#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

Client_ID = "W1TcXyhJTitzD7xIbqeqwQ"
SECRET_ID = "KuchN3CxdZhkpeDyDyQdhi2fjY5VGw"

import requests
from requests import auth
import requests.auth

auth = requests.auth.HTTPBasicAuth(Client_ID, SECRET_ID)

data = {
    'grant_type': 'password',
    'username': 'Wessal-Ayman',
    'password': 'wessal@1511'
}

headers = {'User_Agent': 'MyAPI/0.0.1'}

res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

TOKEN = res.json()['access_token']

headers['Authorization'] = f'bearer {TOKEN}'
