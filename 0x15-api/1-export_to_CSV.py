#!/usr/bin/python3

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    to_do = get('https://jsonplaceholder.typicode.com/todos/')
    to_do_response = to_do.json()
    users = get('https://jsonplaceholder.typicode.com/users/')
    users_response = users.json()


for i in users_response:
    if i.get('id') == int(argv[1]):
        employee = i.get('name')

with open(argv[1] + '.csv', 'w', newline='') as file:
    writ = csv.writer(file, quoting=csv.QUOTE_ALL)

    for i in to_do_response:
        if i['userId'] == int(argv[1]):
            row = [
                i['userId'],
                employee,
                i['completed'],
                i['title']
            ]
            writ.writerow(row)
