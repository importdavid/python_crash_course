# 7-3. Multiples of Ten: pg 117

n = int(input("What is your number?\n"))
if n % 10 == 0:
    print("That is indeed a multiple of 10.")
else:
    print("Not a multiple of 10. Try again.")