#! /usr/bin/env python3
"""Challenge: Capital City Loop."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'

import sys

from pathlib import Path
from random import choice
from yaml import safe_load


def states_capitals(filename='us_capitals.yml') -> tuple:
    """Return a state with its respective capital."""
    try:
        content = Path(filename).read_text()
    except FileNotFoundError as err:
        print(err)
        sys.exit(1)
    else:
        answers = safe_load(content)

    return choice(tuple(answers.items()))


def main():
    """Starting point of the program."""
    state, capital = states_capitals()
    prompt = (f"What is the capital of {state}? (Type 'exit' to quit)\n> ")

    while (answer := input(prompt).lower()) != capital.lower():
        if answer == 'exit':
            print(f'The answer is: {capital!r}.\nGoodbye!')
            break
    else:
        print(f'Correct!')


if __name__ == '__main__':
    main()
