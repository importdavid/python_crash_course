# 7-5. Movie Tickets: pg 123

print("I'm a movie ticket vendor!")
while True:
    age = int(input("What is your age:\n"))
    if age < 3: price = 0
    elif age < 12: price = 10
    else: price = 15
    print(f"That'll be ${price}, please!")