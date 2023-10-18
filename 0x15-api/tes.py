import requests
import sys
import pprint

if __name__ == "__main__":
    user_id = 3 # sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    users_url = requests.get(base_url + 'users/{}'.format(user_id)).json()
    todos_url = requests.get(base_url + 'todos?userId={}'.format(user_id)).json()

    completed_tasks = [task.get('title') for task in todos_url if task.get('completed') is True]
    print(f'Empolyee {users_url.get("name")} is done with tasks({len(completed_tasks)}/{len(todos_url)}):')
    [print('\t {}'.format(task)) for task in completed_tasks]


    # exporting data into csv format
    import csv
    with open('{}.csv'.format(user_id), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, users_url.get('username'), task.get('completed'), task.get('title')]) for task in todos_url]

    # exporting data into json format
    import json
    with open('{}.json'.format(user_id), 'w') as jsonfile:
        json.dump({user_id: [{'task': task.get('title'), 'completed': task.get('completed'), 'username': users_url.get('username')} for task in todos_url]}, jsonfile)


