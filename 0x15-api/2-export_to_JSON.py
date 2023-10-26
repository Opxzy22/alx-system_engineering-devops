#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information about
TODO list progress.
"""

import json
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} EMPLOYEE_ID")
        sys.exit(1)

    employee_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found.")
        sys.exit(1)

    employee_name = response.json().get("name")
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo.get("completed")]
    num_completed_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, num_completed_tasks, total_tasks))
    task_list = []
    for task in todos:
        task_dict = {"task": task.get("title"),
                     "completed": task.get("completed"),
                     "username": employee_name}
        task_list.append(task_dict)
    json_data = {employee_id: task_list}
    with open(f"{employee_id}.json", "w") as outfile:
        json.dump(json_data, outfile)
