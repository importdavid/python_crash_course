"""6-5. Rivers: pg 105
    Make a dictionary containing three major rivers and the country each river 
runs through. One key-value pair might be 'nile': 'egypt'.
    Use a loop to print a sentence about each river, such as "The Nile runs 
through Egypt'.
    Use a loop to print the name of each river included in the dictionary.
    Use a loop to print the name of each country included in the dictionary."""

rivers = {
    'nile': 'egypt',
    'mississippi': 'usa',
    'amazon': 'brazil',
}

for river, country in rivers.items():
    print()
    print(river, country)
    print(f"The {river.title()} river runs through {country.title()}")