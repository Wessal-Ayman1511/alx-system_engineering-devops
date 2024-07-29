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
    
    final_dic = {}
    for i in users_response:
        list = []
        for j in to_do_response:
            dic = {}
            if (i['id'] == j['userId']):
                dic['task'] = j['title']
                dic['completed'] = j['completed']
                dic['username'] = i['username']
                list.append(dic)
        final_dic[i['id']] = list

    json_serialization = json.dumps(final_dic)

    with open('todo_all_employees.json', 'w') as file:
        file.write(json_serialization)
