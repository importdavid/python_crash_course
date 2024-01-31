"""6-2. Favorite Numbers: pg 98
    Use a dictionary to store people's favorite numbers. Think of five names, 
and use them as keys in your dictionary. Think of a favorite number for each 
person, and store each as a value in your dictionary. Print each person's 
name and their favorite number."""

numbers = {
    'David': 7,
    'Emilie': 5,
    'Tom': 3,
    'Stan': 10,
    'Jean': 1,
}

for key, value in numbers.items():
    print(key, value)