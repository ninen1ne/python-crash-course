# 8/5/2024
class User():
    def __init__(self, first_name, last_name, age, gender):
        """A simple attempt to made user profile."""
        self.user_profile = {}
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        """Describe information about each user"""
        self.user_profile['firstname'] = self.first_name
        self.user_profile['lastname'] = self.last_name
        self.user_profile['age'] = self.age
        self.user_profile['gender'] = self.gender
        return self.user_profile

    def greet_user(self):
        """Greeting user with simple msg."""
        print(f'Nice to meet you {self.first_name} {self.last_name}.')

    def increment_login_attempts(self):
        """Increment attribute of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the attribute login_attempts to 0"""
        self.login_attempts = 0


class Privileges():
    """This class only contain prvileges attribute."""

    def __init__(self):
        """Initialize previleges attribute."""
        self.privileges = ['can delete post', 'can ban user', 'can inspect user activities.']

    def show_privileges(self):
        """Show administrator privileges"""
        print('Admin privileges:')
        for privilege in self.privileges:
            print(f'- {privilege}.')


class Admin(User):
    """Model a specific role of special user(admin)."""

    def __init__(self, first_name, last_name, age, gender):
        """Initialize attributes from parent class.
        Then initialize attributes specific to admin role."""
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()


