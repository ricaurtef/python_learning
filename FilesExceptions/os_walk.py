#!/usr/bin/env python3
"""Walking a Directoy Tree."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import os
from pathlib import Path


def main():
    """Entry point."""
    root = Path('TestDir')

    for folder_name, sub_folders, filenames in os.walk(root):
        print(f'The current folder is "{folder_name}"')
        for sub_folder in sub_folders:
            print(f'Subfolder of {folder_name}: {sub_folder}')
        for filename in filenames:
            print(f'File inside {folder_name}: {filename}')
        print()


if __name__ == '__main__':
    main()
