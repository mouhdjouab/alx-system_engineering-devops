#!/usr/bin/python3
"""Exports data in  CSV """

if __name__ == "__main__":

    import csv
    import requests
    import sys

    user_id = sys.argv[1]
    user_emp = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(user_id))
    nome = user_emp.json().get('username')
    to_do = requests.get('https://jsonplaceholder.typicode.com/todos')

    file_name = user_id + '.csv'
    with open(file_name, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in to_do.json():
            if task.get('userId') == int(user_id):
                writer.writerow([user_id, nome, str(task.get('completed')),
                                 task.get('title')])
