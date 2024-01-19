"""11-3. Employee: pg 223
    Write a class called Employee. The __init__() method should take in a 
first name, a last name, and an anuual salary, and store each of these as 
attributes. Write a method called give_raise() that adds $5,000 to the annual 
salary by default but also accepts a different raise amount.
    Write a test file for Employee with two test functions, 
test_five_default_raise() and test_give_custom_raise(). Write your tests once 
without using a fixture, and make sure they both pass. Then write a fixture 
so you don't have to create a new employee instance in each test function. 
Run the tests again, and make sure both tests still pass."""

class Employee:
    """Simple model for an employee with basic salary methods."""

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount