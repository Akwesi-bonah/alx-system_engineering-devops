#!/usr/bin/python3
"""
    Python script that, using this REST API, for a given employee ID,
"""
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    users_url = requests.get(base_url + 'users/{}'
                             .format(user_id)).json()
    todos_url = requests.get(base_url + 'todos?userId={}'
                             .format(user_id)).json()

    with open('{}.csv'.format(user_id), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, users_url.get('username'),
                          task.get('completed'),
                          task.get('title')]) for task in
         todos_url]
