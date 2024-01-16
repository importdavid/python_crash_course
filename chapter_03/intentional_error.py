# Exercise 3-11. Intentional Error: pg 47
# MODIFIED Exercise 3-10. Every Function: pg 45
# Create an intentional index error.

# Programming Languages
pls = ["Python", "JavaScript", "Java", "Ruby", "C++"]

print(f'There are {len(pls)} programming languages in the original list.')
print(sorted(pls))
print(sorted(pls, reverse=True))
print(pls)
pls.sort(reverse=True)
print(pls)
pls.sort()
print(pls)
pls.reverse()
print(pls)

pls.pop()
print(pls)
pls.remove(pls[0])
print(pls)
pls.insert(0, 'Go')
print(pls)
pls.append('Kotlin')
print(pls)
del pls[-1]
print(pls)

# Remove all remaining items and attempt to access an element.
for i in range(len(pls)): pls.pop()

# Intentional error that is caught by try/except logic
try:
    print(pls[0])
except Exception as e:
    print(f'Error: {e}')

# Intentional error that is now commented out
# print(pls[0])