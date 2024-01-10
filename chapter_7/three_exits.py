# 7-6. Three Exits: pg 123
# MODIFIES 7-5. Movie Tickets: pg 123

print("I'm a movie ticket vendor!")

# Stop the loop with a conditional
# 5 tickets available
tickets = 5
while tickets > 0:
    age = int(input("Vendor #1. What is your age:\n"))
    if age < 3: price = 0
    elif age < 12: price = 10
    else: price = 15
    print(f"That'll be ${price}, please!")
    tickets -= 1

# Control the while loop with an 'active' variable
tickets = 5
active = True
while active:
    age = int(input("Vendor #2. What is your age:\n"))
    if age < 3: price = 0
    elif age < 12: price = 10
    else: price = 15
    print(f"That'll be ${price}, please!")
    tickets -= 1
    if tickets == 0: active = False

# break the while loop when the user enters 'quit'
while True:
    age = input("Vendor #3. What is your age:\n('quit' to exit)\n")
    if age == 'quit': break
    age = int(age)
    if age < 3: price = 0
    elif age < 12: price = 10
    else: price = 15
    print(f"That'll be ${price}, please!")
 