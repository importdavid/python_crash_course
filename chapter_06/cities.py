"""6-11. Cities: pg 111
    Make a dictionary called cities. Use the names of three cities as keys in 
your dictionary. Create a dictionary of information about each city and 
include the country that the city is in, its approximate population, and one 
fact about that city. The keys for each city's dictionary should be something 
like country, population, and fact. Print the name of each city and all of the 
information you have stored about it."""

cities = {
    'Detroit': {
        'country': 'USA',
        'population': 2000000,
        'fact': 'Home of the Red Wings.',
    },
    'Melbourne': {
        'country': 'Australia',
        'population': 5000000,
        'fact': 'Kangaroos live here.',
    },
    'Oslo': {
        'country': 'Norway',
        'population': 500000,
        'fact': 'Watch out for Trolls.',
    },
}

for city, info in cities.items():
    print(f"{city.title()}:")
    for key, value in info.items():
        print(f'  {key}: {value}')