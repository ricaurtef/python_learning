#! /usr/bin/env python3
"""Functions: Returning a simple value."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def get_formatted_name(first_name, last_name, middle_name=None):
    """Return a full name, neatly formatted."""
    full_name = f'{first_name} {last_name}'

    if middle_name is not None:
        full_name = f'{first_name} {middle_name} {last_name}'

    return full_name.title()


def main():
    """Entry point."""
    musicians = [('jimi', 'hendrix'), ('john', 'hooker', 'lee')]

    for musician in musicians:
        print(get_formatted_name(*musician))

    while True:
        print("Please tell me your name ('q' to quit): ")

        first_name = input('First name: ')
        if first_name == 'q':
            break

        last_name = input('Last name: ')
        if last_name == 'q':
            break

        formatted_name = get_formatted_name(first_name, last_name)
        print(f'Hello, {formatted_name}!')
        break


if __name__ == '__main__':
    main()
