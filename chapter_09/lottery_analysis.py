"""9-15. Lottery Analysis: pg 180"""

import time
from random import choice

SELECTION = list('0123456789abcde')

def select_ticket():
    ticket = ''
    while len(ticket) < 4:
        ticket += choice(SELECTION)
    return ticket

if __name__ == "__main__":
    """See how long it takes to pick a winner at random from this SELECTION."""
    start = time.time()

    # Winning ticket
    winner = select_ticket()
    print(f"The winning ticket is: {winner}")

    # My ticket
    ticket = select_ticket()
    while ticket != winner:
        ticket = select_ticket()

    end = time.time()
    print(f"Your winning ticket: {ticket}")
    print(f"Took long enough, you lazy winner: {end-start:.4f} seconds")