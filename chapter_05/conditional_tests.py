# Exercise 5-1. Conditional Tests: pg 77

car = 'subaru'
print("Is car == 'subara'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car == 'subaru' or car == 'audi'? I predict True.")
print(car == 'subaru' or car == 'audi')

print("\nHere are 10 more tests. 5 True, 5 False.")
# True
print(car == 'subaru' and len(car) > 4)
print(len(car) > 3)
print('s' in car)
print('u' in car and 'b' in car)
print(car*3 == 'subarusubarusubaru')
# False
print(car == 'bob')
print(car == 'subaru' and car == 'audi')
print(len(car) < 2)
print(car*2 == 'audi')
print(car == True)