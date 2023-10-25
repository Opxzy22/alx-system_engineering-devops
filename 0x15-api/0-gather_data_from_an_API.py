#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    emp_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Employee with ID {} not found.".format(emp_id))
        sys.exit(1)

    employee_name = response.json().get("name")
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)
    response = requests.get(url)
    todos = response.json()
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo.get("completed")]
    num_completed_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}): "
          .format(employee_name, num_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t{}".format(task.get('title')))
