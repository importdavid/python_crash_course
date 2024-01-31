# 9-4. Number Served: pg 166
# MODIFIES 9-1. Restaurant: pg 162

class Restaurant:
    """Model of a simple restaurant."""
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe(self):
        print(f"{self.name} is a restaurant that serves {self.cuisine} dishes!")

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
    restaurant = Restaurant("David's", 'tilapia and eggplant')
    # Original number served
    print(restaurant.number_served)
    # Serve 5 people and manually change number_served
    restaurant.number_served = 5
    print(restaurant.number_served)
    # Change number_served through set_number_served method
    restaurant.set_number_served(10)
    print(restaurant.number_served)
    # Incremenet number_served with final method
    # First, unsuccessfully, then successfully
    restaurant.increment_number_served(-5)
    restaurant.increment_number_served(25)
    print(restaurant.number_served)