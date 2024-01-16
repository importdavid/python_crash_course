# Exercise 4-13. Buffet: pg 67

foods = ("Salad", "Pasta", "Bread Rolls", "Fried Chicken", "Fruit Platter")
for food in foods: print(food)
print()

# Intentional reassignment to throw error, now commented out
# foods[0] = 'Bacon'

# Restaurant menu overhaul, so we reassign entire tuple.
new_menu = ("Salad", "Pasta", "Breadsticks", "Grilled Chicken", "Fruit Platter")
foods = new_menu
for food in foods: print(food)