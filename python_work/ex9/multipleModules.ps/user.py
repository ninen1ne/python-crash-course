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
