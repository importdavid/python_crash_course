"""6-12. Extensions: pg 111
    We're now working with examples that are complex enough that they can be 
extended in any number of ways. Use one of the example programs from this 
chapter, and extend it by adding new keys and values, changing the context 
of the program, or improving the formatting of the output.
    Choosing to extend cities.py. Adding a new dict key 'extension'. Easy."""

cities = {
    'Detroit': {
        'country': 'USA',
        'population': 2000000,
        'fact': 'Home of the Red Wings.',
        'extension': 'Here we goooooooooo!',
    },
    'Melbourne': {
        'country': 'Australia',
        'population': 5000000,
        'fact': 'Kangaroos live here.',
        'extension': 'bouncebouncebounce',
    },
    'Oslo': {
        'country': 'Norway',
        'population': 500000,
        'fact': 'Watch out for Trolls.',
        'extension': 'Trolololololololololol',
    },
}

for city, info in cities.items():
    print(f"{city.title()}:")
    for key, value in info.items():
        print(f'  {key}: {value}')