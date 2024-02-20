#!/usr/bin/python3
" exports data to a JSON "
import json
import requests
import sys


def taskes():
    '''Script that exports all employees TODO tasks to a json file'''

    id = 1
    alltodos = {}
    while True:
        url_web = "https://jsonplaceholder.typicode.com/users/{}".format(id)
        res = requests.get(url_web)
        res_json = res.json()
        if len(res_json) == 0:
            break
        emp_name = res_json.get("name")

        url_web = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            id)
        todos = requests.get(url_web)
        todos_json = todos.json()
        task_list = []

        for task in todos_json:
            task_dict = {}
            task_dict["task"] = task.get("title")
            task_dict["completed"] = task.get("completed")
            task_dict["username"] = emp_name
            task_list.append(task_dict)

        alltodos[id] = task_list
        id += 1

    f_name = "todo_all_employees.json"
    with open(f_name, "a") as fd:
        json.dump(alltodos, fd)


if __name__ == "__main__":
    taskes()
