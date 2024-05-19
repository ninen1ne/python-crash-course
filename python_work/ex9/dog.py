class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(f'{self.name} rolled over!')

dog_00 = Dog('cookie', 7)
dog_00.sit()
dog_00.roll_over()