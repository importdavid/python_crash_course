"""9-14. Lottery: pg 180"""

from random import choice

selection = list('0123456789abcde')

winner = ''
while len(winner) < 4:
    winner += choice(selection)

print(f"The winning ticket is:\n{winner}")