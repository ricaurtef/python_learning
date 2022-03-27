#!/usr/bin/env python3
"""Reading Zip Files."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from pathlib import Path
from zipfile import ZipFile


def main():
    """Entry point."""
    zipname = Path('example.zip')

    with ZipFile(zipname) as zid:
        content = ', '.join(zid.namelist())
        hello_info = zid.getinfo('hello.py')
        eficency = hello_info.file_size / hello_info.compress_size

        print(f'Zip Content: {content}')
        print(f'File name: {hello_info.filename}\n'
              f'File size: {hello_info.file_size}\n'
              f'Compress size: {hello_info.compress_size}\n'
              f'Compressed file is {round(eficency, 2)}x smaller.')

    # The extractall() method for ZipFile objects extracts all the content
    # from a ZIP file into de cwd. Optionally, you can pass a folder name
    # to have it extract the files and folder into it, rather than the cwd.
    # with ZipFile(zipname) as zid:
    #     zid.extractall()  # Optionally a dirname.

    # The extract() method for ZipFile objects will extract a sigle file from
    # the ZIP file.
    # with ZipFile(zipname) as zid:
    #     zid.extract('spam.txt')


if __name__ == '__main__':
    main()
