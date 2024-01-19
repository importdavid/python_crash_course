"""6-9. Favorite Places: pg 111
    Make a dictionary called favorite_places. Think of three names to use as 
keys in the dictionary, and store one to three favorite places for each 
person. Loop through the dictionary, and print each person's name and their 
favorite places."""

favorite_places = {
    'David': ['Australia', 'Norway'],
    'Emilie': ['Norway', 'San Francisco'],
    'Tom': ['Pennsylvania', 'Michigan'],
}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places:")
    for place in places:
        print(f"- {place}")