# 9-3. Users: pg 162

class User:
    """Model of a simple user."""
    def __init__(self, first, last, username, email) -> None:
        self.first = first.title()
        self.last = last.title()
        self.username = username
        self.email = email

    def describe(self):
        print(f"{self.username} is {self.first} {self.last}")
        print(f"Email: {self.email}")

    def greet(self):
        print(f"Hello {self.username}. How are you today?")


if __name__ == "__main__":
    user = User('David', 'Wilkins', 'www', 'email@email.com')
    user.greet()
    user.describe()