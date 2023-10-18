#!/usr/bin/python3
"""
    Python script that, using this REST API, for a given employee ID,
"""

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    users_url = requests.get(base_url + 'users/{}'
                             .format(user_id)).json()
    todos_url = requests.get(base_url + 'todos?userId={}'
                             .format(user_id)).json()

    completed_tasks = [task.get('title') for task in todos_url
                       if task.get('completed') is True]
    print(f'Employee {users_url.get("name")} '
          f'is done with tasks({len(completed_tasks)}'
          f'/{len(todos_url)}):')
    [print('\t {}'.format(task))
     for task in completed_tasks]
