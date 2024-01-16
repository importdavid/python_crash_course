"""10-8. Cats and Dogs: pg 200
    Make two files, cats.txt and dogs.txt. Store at least three names of cats 
in the first file and three names of dogs in the second file. 
    Write a program that tries to read these files and print the contents of 
the file to the screen. Wrap your code in a try-except block to catch the 
FileNotFound error, and print a friendly message if a file is missing. Move 
one of the files to a different location on your system, and make sure the 
code in the except block executes properly.
    *I verified that the try/except block would function properly by moving
a file out of the correct directory."""

from pathlib import Path

paths = [Path('cats.txt'), Path('dogs.txt')]

for path in paths:
    try:
        print(path.read_text())
        # content = path.read_text()
        # print(content)
    except FileNotFoundError:
        print(f"{path} was not found.")