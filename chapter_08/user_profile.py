# 8-13. User Profile: pg 149
# MODIFIES the example program user_profile.py on pg 148

# Import pprint for nicer display
from pprint import pprint as pp

def build_profile(first, last, **user_info):
    """Build a dictionary containing evertyhing we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('David', 'Wilkins',
                             location='Library',
                             field='Python',
                             hobby='Pokemon GO',)

pp(user_profile)