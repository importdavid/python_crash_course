# 7-9. No Pastrami: pg 127
# MODIFIES 7-8. Deli: pg 127

sandwich_orders = ['reuben', 'pastrami', 'pb&j', 'ham and cheese', 'pastrami', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print(f"Finished sandwiches: {finished_sandwiches}")

print("All sandwich orders complete.")