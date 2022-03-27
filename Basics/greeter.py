#!/usr/bin/env python3
"""Defining a Function."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from os import getenv


def greet_user(username: str):
    """Display a simple greeting."""
    print(f'Hello, {username.title()}!')


if __name__ == '__main__':
    greet_user(getenv('USER'))
