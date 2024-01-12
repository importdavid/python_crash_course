"""Checks if given birthday is contained within the first million digits of pi."""

from pathlib import Path

# pi_million_digits.txt
f = '/home/david/edu/python_crash_course/pcc_3e/chapter_10/reading_from_a_file/pi_million_digits.txt'
path = Path(f)

# Create pi string from file
pi = ''
for line in path.read_text().splitlines():
    pi += line.strip()

# Prompt user for birthday and check if it's contained within pi
birthday = input("Enter your birthday in the form mmddyy: ")
if birthday in pi:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Try again, birthday sucker.')