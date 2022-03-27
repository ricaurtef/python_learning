#!/usr/bin/env python3
"""Project: Fetching Current Weather Data."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import requests
from argparse import ArgumentParser


__APP_ID = '2953ee8e1417c8af5d69472180800126'


def args():
    """Handle command-line arguments and options."""
    parser = ArgumentParser(
        prog='weather',
        usage=('%(prog)s <city> <country> [-F]\n\n'
               'EXAMPLE:\n\n%(prog)s "San Francisco" US')
    )
    parser.add_argument('city',
                        help='name of the city whose weather you are \
                              interested in (surround by quotation marks if \
                              the name has spaces)')
    parser.add_argument('country',
                        help='ISO 3166 2-letter Code')
    parser.add_argument('-F', dest='units',
                        action='store_const',
                        const='imperial',
                        default='metric',
                        help='display the temperature in Fahrenheit')

    return parser.parse_args()


def get_weather(location, *, units=None) -> dict:
    """TODO: Write docstrings for this function."""
    symbol = 'K'
    url = (f'https://api.openweathermap.org/data/2.5/weather?q={location}'
           f'&appid={__APP_ID}')

    if units is not None:
        url += f'&units={units}'
        symbol = 'C' if units == 'metric' else 'F'

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    weather_info = dict(
        main=data['weather'][0]['main'],
        description=data['weather'][0]['description'],
        temp=[*data['main'].values()],
        usym=symbol,
    )

    return weather_info


def main():
    """Entry point."""
    argv = args()
    location = f'{argv.city}, {argv.country}'
    units = argv.units

    try:
        weather = get_weather(location, units=units)
    except Exception as error:
        print(error)
    else:
        main = weather['main']
        description = weather['description']
        temp, real, min_temp, max_temp = weather['temp'][:4]
        usym = weather['usym']
        print(
            f'Current weather in {location.title()}: {main} - {description}',
            f'Temperature -> {temp}°{usym}',
            f'Real feel -> {real}°{usym}',
            f'Min temperature -> {min_temp}°{usym}',
            f'Max temperature -> {max_temp}°{usym}', sep='\n'
        )


if __name__ == '__main__':
    main()
