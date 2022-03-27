#! /usr/bin/env python3
"""Challenge: Convert Temperatures.

Simple temperature convertor.
"""
from argparse import ArgumentParser


class Temperature:
    """Simple attempt to model a temperature class."""
    def __init__(self, value):
        """Initialize Temperature class."""
        self.value = value
        self.degrees = ()

    def convert_to_fahrenheit(self):
        """Convert a given value in Celsius to Fahrenheit."""
        self.degrees = ('C', 'F')

        return self.value * (9/5) + 32

    def convert_to_celsius(self):
        """Convert a given value in Fahrenheit to Celsius."""
        self.degrees = ('F', 'C')

        return (self.value - 32) * (5/9)


def args():
    """Handle command line options."""
    parser = ArgumentParser(description='temperature convertor')
    group = parser.add_mutually_exclusive_group(required=True)

    # Temperature value.
    parser.add_argument('value', type=float,
                        help='value to be converted')

    # Conversion options.
    group.add_argument('-f', '--fahrenheit', action='store_true',
                       help='convert to fahrenheit')
    group.add_argument('-c', '--celsius', action='store_true',
                       help='convert to celsius')

    return parser.parse_args()


def main():
    """Starting point of the program."""
    raw_value = args().value
    temperature = Temperature(raw_value)

    if args().fahrenheit:
        converted_value = temperature.convert_to_fahrenheit()
    elif args().celsius:
        converted_value = temperature.convert_to_celsius()

    print(f'{raw_value:.0f}˚{temperature.degrees[0]} = '
          f'{converted_value:.2f}˚{temperature.degrees[1]}')


if __name__ == '__main__':
    main()
