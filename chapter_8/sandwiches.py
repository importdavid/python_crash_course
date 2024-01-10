# 8-12. Sandwiches: pg 149

# Maybe should use more descriptive *ingredients instead of *args
# Although, *args is common usage and representative of lesson
def make_sandwich(*args):
    print("\nMaking a sandwich with:")
    for arg in args:
        print(f'- {arg}')

make_sandwich('bacon', 'lettuce', 'tomato')
make_sandwich('tuna')
make_sandwich('ketchup', 'mustard')