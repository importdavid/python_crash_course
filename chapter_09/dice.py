"""9.13. Dice: pg 180"""

from random import randint

class Die:
    """Representation of a simple die for rolling."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll(self, times):
        for i in range(times):
            print(randint(1,self.sides))


if __name__ == '__main__':
    # Make a 6-sided die and roll it 10 times.
    print("Rolling a 6-sided die 10 times:")
    d = Die()
    d.roll(10)

    # Make a 10-sided die and roll it 10 times.
    print("Rolling a 10-sided die 10 times:")
    d = Die(10)
    d.roll(10)

    # Make a 20-sided die and roll it 10 times.
    print("Rolling a 20-sided die 10 times:")
    d = Die(20)
    d.roll(10)