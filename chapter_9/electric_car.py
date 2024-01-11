# 9-9. Battery Upgrade: pg 173
"""A set of classes that can be used to represent electric cars."""

from car import Car

class Battery:
    """A simple attempt to model a battry for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        if self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar(Car):
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes spcific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


if __name__ == "__main__":
    ec = ElectricCar('ford', 'focus', 2009)
    print(ec.get_descriptive_name())
    ec.battery.describe_battery()
    ec.battery.get_range()
    ec.battery.upgrade_battery()
    ec.battery.get_range()