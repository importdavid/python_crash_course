"""9-12. Multiple Modules: pg 179"""

# Classes were already stored in separate files. Can do this either way.
from admin import Admin, User, Privileges
a = Admin('David', 'Wilkins', 'www', 'email@email.com')
a.privileges.show_privileges()

# import admin, users, privileges
# a = admin.Admin('David', 'Wilkins', 'www', 'email@email.com')
# a.privileges.show_privileges()