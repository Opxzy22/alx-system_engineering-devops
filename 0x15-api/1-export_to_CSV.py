#!/usr/bin/python3
""" pytthon script that export data to csv"""
import csv
import requests
import sys
""" pytthon script that export data to csv"""

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

    with open("{}.csv".format(emp_id), mode="w", newline="") as csv_file:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, quoting=csv.QUOTE_ALL,
                                fieldnames=fieldnames)

        writer.writeheader()
        for todo in todos:
            writer.writerow({
                "USER_ID": emp_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": todo["completed"],
                "TASK_TITLE": todo["title"]
            })

    print("Data exported to {}.csv".format(emp_id))
