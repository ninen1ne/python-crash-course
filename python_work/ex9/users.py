# 8/5/2024
class User():
    def __init__(self, first_name, last_name, age, gender):
        """A simple attempt to made user profile."""
        self.user_profile = {}
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender

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


user00 = User('norawee', 'laohateerapong', 17, 'male')
user00_info = user00.describe_user()
print(user00_info)
user00.greet_user()
print('')
user01 = User('issaret', 'kraibun', 17, 'male')
user01_info = user01.describe_user()
print(user01_info)
user01.greet_user()
print('')
user02 = User('pepe', 'bobo', 60, 'female')
user02_info = user02.describe_user()
print(user02_info)
user02.greet_user()