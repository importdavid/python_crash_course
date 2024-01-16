# 5-8: pg 88
# 5-9: pg 88

# Following line commented out purposefully. Used to test no users case.
# usernames = []
usernames = ['admin', 'user1', 'user2', 'user3', 'user4']

if len(usernames) == 0:
    print('We need to find some users!')
else:
    for name in usernames:
        if name == 'admin':
            print('Hello, boss!')
        else:
            print(f'Hello, {name}.')