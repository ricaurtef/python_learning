#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import csv
from pathlib import Path


def get_higher_scores(csv_file):
    """TODO: Function docstring."""
    higher_scores = {}

    with open(csv_file, mode='r', encoding='utf-8') as fobj:
        csv_reader = csv.reader(fobj, delimiter=',')
        for row in csv_reader:
            if 'name' not in row:
                player = row[0]
                score = int(row[1])
                if score > higher_scores.get(player, 0):
                    higher_scores[player] = score

    return higher_scores


def write_csv(players, filename):
    """TODO: Function docstring."""
    fields = ('Name', 'HighScore')
    with open(filename, mode='w', encoding='utf-8') as fobj:
        csv_writer = csv.DictWriter(fobj, delimiter=',', fieldnames=fields,
                                    quotechar="'")
        csv_writer.writeheader()
        for player, score in players.items():
            csv_writer.writerow({fields[0]: player, fields[1]: score})


def main():
    """Starting point of the program."""
    csv_file = 'scores.csv'
    filename = Path() / 'high_scores.csv'
    players = get_higher_scores(csv_file)

    try:
        if not filename.exists():
            raise FileNotFoundError
    except FileNotFoundError:
        write_csv(players, filename)
        print(f'The "{filename}" file was created successfully.')
    else:
        print(f'The "{filename}" file already exists.')


if __name__ == '__main__':
    main()
