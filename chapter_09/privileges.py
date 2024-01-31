# 9-8. Privileges: pg 173

class Privileges:
    """Class designed to be imported by Admin class to be used
    as an attribute"""
    def __init__(self, *privileges):
        self.privileges = []
        for p in privileges:
            self.privileges.append(p)

    def show_privileges(self):
        print("Admin privileges:")
        for p in self.privileges:
            print(f"\t-{p}")


if __name__ == '__main__':
    p = Privileges(
        'can add post', 
        'can delete post', 
        'can ban user',
        )
    p.show_privileges()