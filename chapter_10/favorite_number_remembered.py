"""10-11. Favorite Number and 10-12. Favorite Number Remembered: pg 206
    If a user's favorite number is already stored, report the favorite number 
to the user. If not, prompt for the user's favorite number and store it in 
a file. Run the program twice to see that it works."""

"""This program could be improved. It should verify the input is a number.
Also, using json seems unnecessary, because the input is so simple."""

from pathlib import Path
import json

path = Path('favorite_number.txt')

if path.exists():
    content = path.read_text()
    number = json.loads(content)
    print(f"I know your favorite number! It's {number}!")
else:
    number = input('What is your favorite number? ')
    s = json.dumps(number)
    path.write_text(s)