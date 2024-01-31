# 7-10. Dream Vacation: pg 127

responses = {}

while True:
    name = input('\nWhat is your name?\n')
    response = input('If you could visit one place in the world, where would you go?\n')
    responses[name] = response
    more = input('Are there any more poll takers? ("no" to quit)\n')
    if more == 'no': break

for name, response in responses.items():
    print()
    print(f"{name.title()} would like to visit {response.title()}.")