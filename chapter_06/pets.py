"""6-8. Pets: pg 111
    Make several dictionaries, where each dictionary represents a different 
pet. In each dictionary, include the kind of animal and the owner's name. 
Store these dictionaries in a list called pets. Next loop through your list 
and as you do, print everything you know about each pet."""

pet1 = {
    'name': 'Ru',
    'owner': 'David',
    'animal': 'python',
    'age': 4
}

pet2 = {
    'name': 'Atlas',
    'owner': 'David',
    'animal': 'cat',
    'age': 3
}

pet3 = {
    'name': 'Pyxis',
    'owner': 'David',
    'animal': 'bearded dragon',
    'age': 5
}

pets = {
    1: pet1,
    2: pet2,
    3: pet3,
}

for pet in pets.values():
    print(f"{pet['owner']} has a {pet['age']}-yr old {pet['animal']} named {pet['name']}.")