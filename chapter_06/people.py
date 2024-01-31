"""6-7. People: pg 111
    Start with the program you wrote for Exercise 6-1 (page 98). Make two new 
dictionaries representing different people, and store all three dictionaries 
in a list called people. Loop through your list of people. As you loop through 
the list, print everything you know about each person."""

person1 = {
    'first': 'Emilie',
    'last': 'Samuelsen',
    'age': 35,
    'city': 'San Francisco'
}

person2 = {
    'first': 'David',
    'last': 'Wilkins',
    'age': 32,
    'city': 'Melbourne'
}

person3 = {
    'first': 'Tom',
    'last': 'Christopher',
    'age': 68,
    'city': 'Des Moines'
}

people = {
    1: person1,
    2: person2,
    3: person3,
}

for person in people.values():
    print(f"{person['first']} {person['last']} is {person['age']} and lives in {person['city']}.")