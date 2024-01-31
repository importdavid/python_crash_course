import random

# Potential invitees to dinner.
invitees = ['Emilie', 'Leonardo Da Vinci', 'Jesus']

# Invites each member of given list to a dinner party.
def invite(invitees):
    for invitee in invitees:
        message = f'{invitee}, would you like to have dinner at my place tonight?'
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

if __name__=="__main__":
    main()