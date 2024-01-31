"""10-9. Silent Cats and Dogs: pg 200
    Modify your except block in 10-8 to fail silently if either file is missing.
    *Verified that the programs works like last exercise, only fails silently."""

from pathlib import Path

paths = [Path('cats.txt'), Path('dogs.txt')]

for path in paths:
    try:
        print(path.read_text())
        # content = path.read_text()
        # print(content)
    except FileNotFoundError:
        pass
        # print(f"{path} was not found.")