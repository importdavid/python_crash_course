"""10-2. pg 190. Reads learning_python.txt and then replaces 'Python'
text with 'C'. Only print modified lines."""

from pathlib import Path

path = Path('learning_python.txt')
for line in path.read_text().splitlines():
    if 'Python' in line:
        line.replace('Python', 'C')
        print(line)

# contents = path.read_text().replace('Python', 'C')
# print(contents)