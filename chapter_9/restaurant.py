# 9-1. Restaurant: pg 162

class Restaurant:
    """Model of a simple restaurant."""
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        print(f"{self.name} is a restaurant that serves {self.cuisine} dishes!")

    def open(self):
        print(f"{self.name} is open!")

if __name__ == '__main__':
    r = Restaurant("David's", 'tilapia and eggplant')
    r.describe()
    r.open()