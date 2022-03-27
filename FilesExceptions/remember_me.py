#!/usr/bin/env python3
"""remember_me

Load the username, if it has been stored previously. Otherwise, prompt
for the username and store it.
"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import json


def get_stored_username(file_):
    """Get stored username if available."""
    try:
        with open(file_) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username(file_):
    """Prompt for a new username."""
    username = input('What is your name? ')

    with open(file_, mode='w') as f:
        json.dump(username, f)

    return username


def main():
    """Entry point."""
    filename = 'username.json'
    username = get_stored_username(filename)

    if username is not None:
        print(f'Welcome back, {username.title()}!')
    else:
        username = get_new_username(filename)
        print(f'We will remember you when you come back, {username.title()}!')


if __name__ == '__main__':
    main()
