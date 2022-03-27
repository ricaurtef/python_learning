#!/usr/bin/env python3
"""health_check.py: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import shutil

import psutil


def sane_disk_usage(disk='/'):
    """TODO."""
    disk_usage = shutil.disk_usage(disk)
    free_percent = round((disk_usage.free/disk_usage.total) * 100, 2)

    return free_percent > 20


def sane_cpu_usage():
    """TODO."""
    usage = psutil.cpu_percent(1)

    return usage < 75


def main():
    """Starting point of the program."""
    if not sane_disk_usage():
        print('Warning: less than 20% free disk space.')
    elif not sane_cpu_usage():
        print('Warning: CPU usage over 75%.')
    else:
        print('Everything is OK!')


if __name__ == '__main__':
    main()
