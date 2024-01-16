# Exercise 4-12. More Loops: pg 65

# foods.py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
friend_foods.append('bacon')

print('My favorite foods are:')
for i in my_foods: print(i)
print("My friend's favorite foods are:")
for i in friend_foods: print(i)