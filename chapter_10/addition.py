"""10-6. Addition: pg 200
    One common problem when prompting for numerical input occurs when people provide text instead 
of numbers. When you try to convert the input to an int, you'll get a ValueError.
    Write a program that prompts for two numbers. Add them together and print the result. 
Catch the ValueError if either input value is not a number, and print a firendly error message. 
Test your program by entering two numbers and then b entering some text instead of a number."""

addends = []
while len(addends) < 2:
    try:
        addend = float(input('Please input a number: '))
    except ValueError:
        print('A NUMBER, noob!')
    else:
        addends.append(addend)

print(f"The sum of those two numbers is {sum(addends)}.")