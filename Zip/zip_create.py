#!/usr/bin/env python3
"""Creating and Adding to ZIP Files."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import zipfile
from pathlib import Path


def main():
    """Entry point."""
    zipname = Path('example02.zip')
    dirname = Path('TestDir')

    if not zipname.exists():
        with zipfile.ZipFile(zipname, mode='w') as zid:
            for file_ in dirname.rglob('*'):
                if file_.is_file():
                    zid.write(file_, compress_type=zipfile.ZIP_DEFLATED)

    # List zip file content.
    with zipfile.ZipFile(zipname) as zid:
        content = '\n'.join(zid.namelist())

        print(f'"{zipname}" content:\n{content}')


if __name__ == '__main__':
    main()
