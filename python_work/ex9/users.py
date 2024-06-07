# This program show information about each users and sent a simple message.
# Create class User for storing user informations and send message to each person.
# 23/3/2024

class User():
    """Describe information about each user and greet them."""
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 

    def describe_user(self):
        """Prints a summary of the user's information."""
        print("\nThe information about person:")
        print("Name: " + self.first_name.title() +' ' +  self.last_name.title())
        print("Age: " + str(self.age))


    def greet_user(self):
        """Print individual message for each person."""
        msg = "it's been a while since we meet each other am I right " + self.first_name.title() + '?'
        print('message: ' + msg)

user_1 = User('norawee', 'laohateerapong', 17)

user_2 = User('issaret', 'kraibun', 20)


user_1.describe_user()
user_1.greet_user()


user_2.describe_user()
user_2.greet_user()

