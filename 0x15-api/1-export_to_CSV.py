#!/usr/bin/python3
" script  export data in CSV "
import requests
import sys


def taskes(id):
    '''exports an employee  tasks to  csv

    '''

    web_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    res = requests.get(web_url)
    res_json = res.json()
    employee_name = res_json["name"]

    web_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    to_dos = requests.get(web_url)
    to_dos_json = to_dos.json()
    number_tasks = len(to_dos_json)

    task_compleated = 0
    task_list = ""

    f_name = "{}.csv".format(id)

    with open(f_name, "a") as fd:
        for todo in to_dos_json:
            completed = todo.get("completed")
            title = todo.get("title")
            csv_data = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(id,
                                                              employee_name,
                                                              completed,
                                                              title
                                                              )
            fd.write(csv_data)


if __name__ == "__main__":
    taskes(sys.argv[1])
