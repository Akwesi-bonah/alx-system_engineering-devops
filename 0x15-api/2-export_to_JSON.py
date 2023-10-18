#!/usr/bin/python3
"""
    Python script that, using this REST API, for a given employee ID,
"""


import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    users_url = requests.get(base_url + 'users/{}'
                             .format(user_id)).json()
    todos_url = requests.get(base_url + 'todos?userId={}'
                             .format(user_id)).json()

    with open('{}.json'.format(user_id), 'w') as jsonfile:
        json.dump({user_id: [
            {'task': task.get('title'), 'completed': task.get('completed'),
             'username': users_url.get('username')} for
            task in todos_url]}, jsonfile)
