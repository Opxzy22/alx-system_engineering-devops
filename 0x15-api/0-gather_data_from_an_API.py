import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'

    emp_id = sys.argv[1]
    employee_url = '{}/user/{}'.format(url, emp_id)
    response = requests.get(employee_url)
    if response.status_code !=200:
        print("error employee id with id {} not found".format(emp_id))
        sys.exit(1)

    employee_data = response.json()
    employee_name = response.json.get("name")

    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)
    todo_response = requests.get(todo_url)
    if todo_response.status_code !=200:
        print("failed to retrieved todo list for employee: {}".format(employee_name))
        sys.exit(1)

    todos = todo_response.json()
    total_task = len(todos)
    task_completed = [task for task in total_task if task.get('completed')]
    num_of_task_completed = len(task_completed)

    print("employee {} is done with {}/{}".format(employee_name, task_completed, total_task))
    for task in completed_tasks:
            print("\t{}".format(task.get('title')))
