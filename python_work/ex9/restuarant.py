# Program show general information about restuarant.
# This program simulated bihavior of restuarant as an object.
# Try to code oop way using class.
# 22/3/2024

class Restuarant():
    """"""

    def __init__(self, restuarant_name, cuisine_type):
        """Initialize name and cuisine_type attributes."""
        self.restuarant_name = restuarant_name
        self.cuisine_type = cuisine_type

    def describe_restuarant(self):
        """Describe general information about my restuarant."""
        print("\nMy restuarant: ")
        print(self.restuarant_name.title())
        print("Cuisine type: " + self.cuisine_type.title())

    def open_restuarant(self):
        """To indicated that the restuarant is open or not."""
        print("Status of restuarant: " + self.restuarant_name.title() + " is now open.")

my_restuarant = Restuarant('pepebobo', 'italian cuisine')
my_restuarant.describe_restuarant()
my_restuarant.open_restuarant()
