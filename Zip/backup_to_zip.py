#!/usr/bin/env python3
"""
Copies an entire folder and its contents into a ZIP file whose filename
increments.
"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import zipfile as zf
from pathlib import Path

# TODO: Write the command-line interface.


def get_backup_name(dirname):
    """Determine the name of the backup file."""
    format_num = 0

    # Figure out the filename based on what files already exist.
    while True:
        zipname = Path(f'{dirname}_{format_num:02d}.zip')
        if not zipname.exists():
            break
        format_num += 1

    return str(zipname).lower()


def backup_zip(dirname):
    """Backup the entire contents of 'dirname' into a ZIP file."""
    dir_ = Path(dirname)
    zipname = get_backup_name(dirname)

    with zf.ZipFile(zipname, 'w') as zid:
        print(f'Creating {zipname}...')
        for file_ in dir_.rglob('*'):
            if file_.suffix != '.zip':
                print(f'Adding {file_} to {zipname}...')
                zid.write(file_, compress_type=zf.ZIP_DEFLATED)
        print('Done.')


def main():
    """Entry point."""
    backup_zip('TestDir')


if __name__ == '__main__':
    main()
