"""Write a while loop that prompts users for their name. Collect all the names that are entered,
and then write these names to a file called guest_book.txt. Make sure each entry appears on
a new line in the file."""

from pathlib import Path

with Path('guest_book.txt').open('a') as path:
    print('Enter q to quit')
    while True:
        name = input('What is your name? ')
        if name == 'q': break
        path.write(name + '\n')