#!/usr/bin/python3

"""
The module provides a function to export all tasks to a JSON file.
"""

import lazy_methods


if __name__ == "__main__":
    # gets user info and todos once so we can minimize the number of requests.
    # this helps to achieve more speed since everything will be done locally.
    # after the data has been retrieved.
    users = lazy_methods.get_users()
    todos = lazy_methods.get_todos()
    lazy_methods.export_all_to_json(users=users, tasks=todos)
