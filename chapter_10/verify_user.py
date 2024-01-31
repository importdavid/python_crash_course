"""10-14. Verify User: pg 206
    The final listing for remember_me.py assumes either that the user has 
already entered their username or that the program is running for the first 
time. We should modify it in case the current user is not the person who 
last used the program. 
    Before printing a welcome back message in greet_user(), ask the user if 
this is the correct username. If it's not, call get_new_username() to get 
the correct username."""

from pathlib import Path
import json

def get_stored_user(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None
    
def get_new_user(path):
    """Prompt for new user info."""
    username = input("What is your name? ")
    email = input("What is your email? ")
    nickname = input("What is your nickname? ")
    user = {
        'username': username,
        'email': email,
        'nickname': nickname,
    }
    contents = json.dumps(user)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {user['username']}!")
    return user

def greet_user():
    """Greet the user by name."""
    path = Path('user.json')
    user = get_stored_user(path)
    if user:
        verify = input(f"Are you {user['username']}? (y/n) ")
        if verify == 'y':
            print(f"Welcome back, {user['username']}!")
            print(user)
        else:
            get_new_user(path)
    else:
        get_new_user(path)


if __name__ == "__main__":
    greet_user()