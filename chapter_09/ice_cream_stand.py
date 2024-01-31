# 9-6. Ice Cream Stand: pg 173
# IMPORTS from 9-1. Restaurant: pg 162

from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """Simple model of an ice cream stand. Inherits from Restaurant class."""
    def __init__(self, name, cuisine='Ice Cream'):
        super().__init__(name, cuisine)
        self.flavors = [
            'strawberry', 
            'mango', 
            'chocolate',
            'moose tracks',
            ]
        
    def list_flavors(self):
        print("We have these flavors to choose from:")
        for flavor in self.flavors:
            print(f"\t-{flavor}")


if __name__ == '__main__':
    stand = IceCreamStand("David's")
    stand.describe()
    stand.open()
    stand.list_flavors()