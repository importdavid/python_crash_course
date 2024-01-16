# Exercise 5-6. Stages of Life: pg 84

age = int(input("How old are you?\n"))

if age < 2:
    print('You a baby!')
elif age < 4:
    print('You a toddler!')
elif age < 13:
    print('You a kid!')
elif age < 20:
    print('You a teenager!')
elif age < 65:
    print('You a adult!')
else:
    print('You old!')