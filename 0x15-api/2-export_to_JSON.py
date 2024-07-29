#!/usr/bin/python3
"""
Python script that exports data in the CSV format
"""

from requests import get
from sys import argv
import json


if __name__ == "__main__":
    to_do = get('https://jsonplaceholder.typicode.com/todos/')
    to_do_response = to_do.json()
    users = get('https://jsonplaceholder.typicode.com/users/')
    users_response = users.json()

    for i in users_response:
        if i['id'] == int(argv[1]):
            user_name = i['username']
            user_id = i['id']

    list = []

    for i in to_do_response:

        dic = {}
        if i['userId'] == int(argv[1]):
            dic['task'] = i['title']
            dic['completed'] = i['completed']
            dic['username'] = user_name
            list.append(dic)
    dict = {}
    dict[user_id] = list
    json_serialization = json.dumps(dict)

    with open(argv[1] + ".json", 'w') as file:
        file.write(json_serialization)
