# Program show general information about restuarant.
# This program simulated bihavior of restuarant as an object.
# Create three difference instances from the class and call describe_restuarant for each method.
# Try to code oop way using class.
# 23/3/2024

class Restuarant():
    """"""

    def __init__(self, restuarant_name, cuisine_type):
        """Initialize name and cuisine_type attributes."""
        self.restuarant_name = restuarant_name
        self.cuisine_type = cuisine_type

    def describe_restuarant(self):
        """Describe general information about my restuarant."""
        print("\n" + self.restuarant_name.title())
        print("Cuisine type:" + self.cuisine_type.title())

    def open_restuarant(self):
        """To indicated that the restuarant is open or not."""
        print("Status of restuarant: " + self.restuarant_name.title() + " is now open.")

monazt = Restuarant('monazt', 'italian cuisine')
monazt.describe_restuarant()

heuagomundo = Restuarant('heuagomundo', 'japanese cuisine')
heuagomundo.describe_restuarant()

amsterdam_shaw = Restuarant('amsterdam shaw', 'dutch cuisine')
amsterdam_shaw.describe_restuarant()