"""10-7. Addition Calculator: pg 200
Wrap your code from Exercise 10-6 in a while loop so the user can continue 
entering numbers, even if they make a mistake and enter text instead of a 
number.
I changed the loop to 'while True' to add any amount of addends."""

addends = []
print("Enter q to finish entering addends.")

while True:
    try:
        addend = input('Enter a number: ')
        if addend == 'q': break
        addend = float(addend)
    except ValueError:
        print('A NUMBER, noob!')
    else:
        addends.append(addend)

print(f"The sum of those numbers is {sum(addends)}.")