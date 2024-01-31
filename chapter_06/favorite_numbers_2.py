"""6-10. Favorite Numbers 2: pg 111
    Modify your program from Exercise 6-2 (page 98) so each person can have 
more than one favorite number. Then print each person's name along with their 
favorite numbers."""

numbers = {
    'David': [1,2,3],
    'Emilie': [5],
    'Tom': [4,6],
    'Stan': [10],
    'Jean': [4,5,6,7,8,9],
}

for name, nums in numbers.items():
    print(f"{name}'s favorite numbers:")
    print(nums)