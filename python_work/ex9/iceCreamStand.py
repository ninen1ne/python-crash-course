# 8/5/2024
class Restuarant():
    """Simulate simple restuarant."""
    def __init__(self, restuarant_name, cuisine_type):
        """Initialize restuarant_name and cuisine_type attributes."""
        self.restuarant_name = restuarant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restuarant(self):
        """Describe information about restuarant."""
        print(f'Restuarant name is: {self.restuarant_name}.')
        print(f'Type of cuisine is: {self.cuisine_type} cuisine.') 

    def open_resruarant(self, date):
        """Tell that restuarant is now open or not."""
        if date.title() == 'Mon' or date.title == 'Tue' or date.title() == 'Wed' or date.title()==  'Thu' or date.title() ==  'Fri':
            print('Restuarant is now open(10.00 AM - 5.00 PM).')
        elif date.title() == 'Sat' or date.title() == 'Sun':
            print('Restuarant is close for saturday and sunday.')
        else:
            print('Invalid date!!!')

    def set_number_served(self, number_served):
        """Set the number of customer that has served."""
        if number_served >= self.number_served:
            self.number_served = number_served
        elif number_served < self.number_served:
            print('Can\'t enter number lower than exist number served attribute!')
        else:
            print('You can enter only integer!')

    def increment_number_served(self, addiontal_served):
        """Add the given amount of number to number_served attribute."""
        if addiontal_served >= 0:
            self.number_served += addiontal_served
        elif addiontal_served < 0:
            print('You can\'t enter number that lower than 0.')
        else:
            print('You can only enter integer.')
            

class IceCreamStand(Restuarant):
    """Child class of restuarant specific to icecream."""

    def __init__(self, restuarant_name, cuisine_type):
        """Initialize attributes of the restuarant class.
           Then initialize attributes specific to an ice cream stand."""
        super().__init__(restuarant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'lemon']

    def display_flavors(self):
        """Display all ice cream flavors aviable in ice cream stand."""
        print('Ice cream flavors list:')
        for flavor in self.flavors:
            print(f'- {flavor}.')

my_iceCream = IceCreamStand('cocoa', 'italian')
my_iceCream.display_flavors()
my_iceCream.describe_restuarant()
