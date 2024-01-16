# 9-1. Restaurant: pg 162

class Restaurant:
    """Model of a simple restaurant."""
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        print(f"{self.name} is a restaurant that serves {self.cuisine}!")

    def open(self):
        print(f"{self.name} is open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        if increment > 0:
            self.number_served += increment
        else:
            print("That value does not increment number_served.")

if __name__ == '__main__':
    r = Restaurant("David's", 'tilapia and eggplant')
    r.describe()
    r.open()