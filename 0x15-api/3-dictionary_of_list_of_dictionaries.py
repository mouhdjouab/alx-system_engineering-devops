#!/usr/bin/python3
"""Exports  in  JSON """

if __name__ == "__main__":

    import json
    import requests
    import sys

    user = requests.get("https://jsonplaceholder.typicode.com/users")
    user = user.json()
    tod_os = requests.get('https://jsonplaceholder.typicode.com/todos')
    tod_os = tod_os.json()
    todo_All = {}

    for user in user:
        tasks = []
        for task in tod_os:
            if task.get('userId') == user.get('id'):
                tasks_Dict = {"username": user.get('username'),
                              "task": task.get('title'),
                              "completed": task.get('completed')}
                tasks.append(tasks_Dict)
        todo_All[user.get('id')] = tasks

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todo_All, f)
