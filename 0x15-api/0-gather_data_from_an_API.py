#!/usr/bin/python3
"""Returns  list information for employee ID."""
import requests
import sys


def taskes(id):
    '''displays an employee completed tasks

    '''

    url_web = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    response = requests.get(url_web)
    response_json = response.json()
    employee_name = response_json.get("name")

    url_web = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    to_do_s = requests.get(url_web)
    todos_json = to_do_s.json()
    n_tasks = len(todos_json)

    task_compleated = 0
    task_list = ""

    for task in todos_json:
        if task.get("completed") is True:
            task_compleated += 1
            task_list += "\t " + task.get("title") + "\n"

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          task_compleated,
                                                          n_tasks))
    print(task_list[:-1])


if __name__ == "__main__":
    taskes(sys.argv[1])
