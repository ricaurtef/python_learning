"""A set of classes used to represent gas and electric cars."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def __repr__(self):
        """Return a neatly formatted descriptive name."""
        long_name = f'{self.year} {self.manufacturer} {self.model}'

        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cannot roll back an odometer!')

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles > 0:
            self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f'This car has a {self.battery_size}-KWh battery.')

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range_ = 260
        elif self.battery_size == 100:
            range_ = 315

        print(f'This car can go about {range_} miles on a full charge.')


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        The initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()
