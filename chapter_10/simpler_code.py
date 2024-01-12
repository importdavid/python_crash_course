"""10-3. pg 190. Remove the temporary variable, lines, in file_reader.py
with code that simply loops over the list returned from .splitlines()."""

# Original file_reader.py
# from pathlib import Path
# path = Path('pi_digits.txt')
# contents = path.read_text()
# lines = contents.splitlines()
# for line in lines:
#     print(line)

# Simplified code
from pathlib import Path
path = Path('pi_digits.txt')
lines = path.read_text().splitlines()
for line in lines:
    print(line)