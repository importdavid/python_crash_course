# Exercise 4-10. Slices: pg 65
# MODIFIES Exercise 4-9. Cube Comprehension: pg 60

cubes = [i**3 for i in range(1,11)]

print(f"The first three items in the list are: {cubes[0:3]}")
print(f"The items from the middle of the list are: {cubes[3:6]}")
print(f"The last three items in the list are: {cubes[-3:]}")
