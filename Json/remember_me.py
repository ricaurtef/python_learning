#!/usr/bin/env python3
"""remember_me.py: playing with the json module.

Load the username, if it has been stored previously. Otherwise, prompt
for the username and store it.
"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import json


def get_stored_username(filename):
    """Get stored username if available."""
    try:
        with open(filename, mode='r') as fobj:
            username = json.load(fobj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username(filename):
    """Prompt for a new username and store it in a .json file."""
    username = input('What is your name? ').lower()

    with open(filename, mode='w') as fobj:
        json.dump(username, fobj)

    return username


def main():
    """Starting point of the program."""
    filename = 'username.json'
    username = get_stored_username(filename)

    if username is not None:
        print(f'Welcome back, {username.title()}!')
    else:
        username = get_new_username(filename)
        print(f'We\'ll remember you when you come back, {username.title()}!')


if __name__ == '__main__':
    main()
