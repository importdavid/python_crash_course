# Exercise 3-10. Every Function: pg 45
# Use every function introduced in chapter 3 on a list of your own design

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