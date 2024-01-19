# 9-5. Login Attempts: pg 167
# MODIFIES 9-3. Users: pg 162

class User:
    """Model of a simple user."""
    def __init__(self, first, last, username, email) -> None:
        self.first = first.title()
        self.last = last.title()
        self.username = username
        self.email = email
        self.login_attempts = 0

    def describe(self):
        print(f"{self.username} is {self.first} {self.last}")
        print(f"Email: {self.email}")

    def greet(self):
        print(f"Hello {self.username}. How are you today?")

    def increment_login_attempts(self, increment=1):
        self.login_attempts += increment
    
    def reset_login_attempts(self):
        self.login_attempts = 0


if __name__ == "__main__":
    user = User('David', 'Wilkins', 'www', 'email@email.com')
    user.greet()
    user.describe()

    # Exercise 9-5 added procedure
    for i in range(42): user.increment_login_attempts()
    print(user.login_attempts)
    user.reset_login_attempts()
    print(user.login_attempts)