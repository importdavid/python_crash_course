# 9-7. Admin: pg 173
# Imports User class from 9-3. users.py
# show_privileges method moved to privileges.py as per 9-8.
# Imports Privileges class from 9-8. privileges.py

from users import User
from privileges import Privileges

class Admin(User):
    """Simple model of an administrator. Inherits from User class."""
    def __init__(self, first, last, username, email):
        super().__init__(first, last, username, email)
        self.privileges = Privileges(
                            'can ban users', 
                            'can modify posts',
                            )
    
    # def show_privileges(self):
    #     print("Admin privileges:")
    #     for privilege in self.privileges:
    #         print(f"\t-{privilege}")


if __name__ == '__main__':
    a = Admin('David', 'Wilkins', 'www', 'email@email.com')
    a.describe()
    a.privileges.show_privileges()