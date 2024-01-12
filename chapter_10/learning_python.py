"""10-3. pg 189. Reads learning_python.txt and prints the contents in two ways."""

from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print(contents)
for line in contents.splitlines():
    print(line)