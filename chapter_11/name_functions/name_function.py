"""First example foray into testing Python code with pytest. Pg 211-217."""

def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

if __name__ == '__main__':
    print("Enter 'q' at any time to quit.")
    while True:
        first = input('\nPlease give me a first name: ')
        if first == 'q':
            break
        last = input('\nPlease give me a last name: ')
        if last == 'q':
            break
        
        formatted_name = get_formatted_name(first, last)
        print(f"\tNeatly formatted name: {formatted_name}.")