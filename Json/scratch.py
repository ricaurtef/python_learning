#!/usr/bin/env python3
"""Working with JSON.

For your introductory example, you’ll use JSONPlaceholder:
https://jsonplaceholder.typicode.com/, a great source of
fake JSON data for practice purposes.
"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import json
import requests


def main():
    """Starting point of program execution."""
    api = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(api)
    todos = json.loads(response.text)

    print(todos[:10])


if __name__ == '__main__':
    main()
