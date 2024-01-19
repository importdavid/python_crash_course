"""
9-11. Imported Admin: pg 179
Both the commented and uncommented sections can be used interchangeably.
admin.py imports both the User and Privileges classes, so all exist within.
"""

# import admin, users, privileges
# a = admin.Admin('David', 'Wilkins', 'www', 'email@email.com')
# a.privileges.show_privileges()

from admin import Admin, User, Privileges
a = Admin('David', 'Wilkins', 'www', 'email@email.com')
a.privileges.show_privileges()