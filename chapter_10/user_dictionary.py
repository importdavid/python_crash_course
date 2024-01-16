"""10-13. User Dictionary: pg 206
    The remember_me.py example only stores one piece of information, the 
username. Expand this example by asking for two more pieces of information 
about the user, then store all the information you collect in a dictionary. 
Write this dictionary to a file using json.dumps(), and read it back in 
using json.loads(). Print a summary showing exactly what your program 
remembers about the user."""

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
    return user

def greet_user():
    """Greet the user by name."""
    path = Path('user.json')
    user = get_stored_user(path)
    if user:
        print(f"Welcome back, {user['username']}!")
        print(user)
    else:
        user = get_new_user(path)
        print(f"We'll remember you when you come back, {user['username']}!")


if __name__ == "__main__":
    greet_user()