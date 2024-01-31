# Exercise 4-2. Animals: pg 56

animals = ['cat', 'dog', 'goat', 'ox']

for animal in animals:
    message = 'A'
    if animal.lower()[0] in 'aeiou': message += 'n'
    message = message + (f' {animal} would make a great pet!')
    print(message)