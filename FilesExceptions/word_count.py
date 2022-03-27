#!/usr/bin/env python3
"""Handling Exceptions: FileNotFoundError."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from pathlib import Path


def count_words(filename):
    """Count the approximate number of words in a file."""
    filename = Path() / filename
    try:
        content = filename.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'Sorry, the file "{filename.name}" does not exist.')
    else:
        # Count the approximate number of words in the file.
        num_words = len(content.split())
        print(f'The file "{filename.name}" has about {num_words} words.')


def main():
    """Entry point."""
    filenames = (
        'alice_in_wonderland.txt',
        'siddhartha.txt',
        'moby_dick.txt',
        'little_women.txt',
    )

    for filename in filenames:
        count_words(filename)


if __name__ == '__main__':
    main()
