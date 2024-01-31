# Exercise 3-9. Dinner Guests: pg 45
# MODIFIED Exercise 3-7. Shrinking Guest List: pg 42

import random

# Potential invitees to dinner.
invitees = ['Emilie', 'Leonardo Da Vinci', 'Jesus']

# Invites each member of given list to a dinner party.
def invite(invitees):
    
    # ONLY the following line was added:
    print(f'Inviting {len(invitees)}:')

    for invitee in invitees:
        message = f'{invitee}, would you like to have dinner with me and friends?'
        print(message)
    print()

def main():
    # Invite each of these potential invitees to dinner.
    invite(invitees)

    # One of your invitees cannot attend. Chosen by random module.
    no_show = random.choice(invitees)
    message = f'{no_show} cannot attend.'
    print(message)

    # Modify invitee list and invite Jeff Probst, instead.
    invitees.remove(no_show)
    new_invitee = 'Jeff Probst'
    invitees.append(new_invitee)
    invite(invitees)

    # Notify guests that you found a bigger table. 
    # Add three new invitees with different methods.
    # Invite everyone to dinner again.
    print('Everyone, I found a bigger table!')
    invitees.insert(0, 'Dad')
    invitees.insert(2, 'Charles Hoskinson')
    invitees.append('Sid')
    invite(invitees)

    # Now the new table won't arrive in time for dinner.
    # Notify everyone that there is now only space for two guests.
    print("Everyone, new table complications. Now we must have a walking taco bar!")
    print("But for the programming exercise, here is the actual assignment:")

    # Pop invitees from the invitee list until only two remain.
    # Inform and apologize to each popped invitee.
    for i in range(len(invitees) - 2):
        reject = invitees.pop()
        message = f"Sorry, {reject}, I must implore you to stay home tonight."
        print(message)
    print()

    # Invite the remaining two invitees.
    invite(invitees)

    # Use del to remove last to invitees and print the empty list to verify.
    del invitees[0]; del invitees[0]
    print(invitees)

if __name__=="__main__":
    main()
    print("Let's eat!")