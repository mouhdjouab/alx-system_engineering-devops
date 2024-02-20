#!/usr/bin/python3
"exports data to  JSON "
import json
import requests
import sys


def takses(id):
    '''exports an employee  tasks to  json

    '''

    url_web = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    res = requests.get(url_web)
    res_json = res.json()
    emp_nale = res_json.get("name")

    url_web = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    to_dos = requests.get(url_web)
    to_dos_json = to_dos.json()
    taskslist = []

    for task in to_dos_json:
        task_dict = {}
        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = emp_nale
        taskslist.append(task_dict)

    to_dos = {"{}".format(id): taskslist}

    file_name = "{}.json".format(id)
    with open(file_name, "a") as fd:
        json.dump(to_dos, fd)


if __name__ == "__main__":
    takses(sys.argv[1])
