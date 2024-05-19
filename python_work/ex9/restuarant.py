# 8/5/2024
class Restuarant():
    """Simulate simple restuarant."""
    def __init__(self, restuarant_name, cuisine_type):
        """Initialize restuarant_name and cuisine_type attributes."""
        self.restuarant_name = restuarant_name.title()
        self.cuisine_type = cuisine_type

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

choice = 1

print('This program will allow you to know more about restuarant and check it status.')
print('(press "0" at any time to quit.)')

while choice != 0:
    name = input('Enter restuarant name: ')
    if name == '0':
        break
    cuisine = input('Enter your restuarant cuisine type: ')
    if name == '0':
        break
    my_restuarant = Restuarant(name, cuisine) # create instance from Restuarant class.
    print('---------------')
    print('1, for describe_restuarant.')
    print('2, for check status restuarant.')
    print('0, for exit program.')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        my_restuarant.describe_restuarant()
    elif choice == 2:
        date = input('Enter date for check restuarant status(Mon-Sun): ')
        my_restuarant.open_resruarant(date)
    elif choice == 0:
        print('Exiting program...')
    else:
        print('Invalid choice!')