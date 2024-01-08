# Exercise 4-11. My Pizzas, Your Pizzas: pg 65
# MODIFIES Exercise 4-1. Pizzas: pg 56

pizzas = ['pepperoni', 'mushroom', 'onion']
friend_pizzas = pizzas[:]

pizzas.append('anchovy')
friend_pizzas.append('bacon')

print('My favorite pizzas are:')
for pizza in pizzas: print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas: print(pizza)