#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    user_id = sys.argv[1]
    user_emp = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(user_id))
    to_dos = requests.get('https://jsonplaceholder.typicode.com/todos')
    to_dos = to_dos.json()

    todo_User = {}
    task_List = []

    for task in to_dos:
        if task.get('userId') == int(user_id):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user_emp.json().get('username')}
            task_List.append(taskDict)
    todo_User[user_id] = task_List

    file_name = user_id + '.json'
    with open(file_name, mode='w') as f:
        json.dump(todo_User, f)
