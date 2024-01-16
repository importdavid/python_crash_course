"""Prompt the user for their name. When they respond, write their name 
to a file called guest.txt."""

from pathlib import Path

name = input("What is your name? ")
path = Path('guest.txt')
path.write_text(name)