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
    print('3, for show and modify number of customers that resterrant has served.')
    print('0, for exit program.')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        my_restuarant.describe_restuarant()
    elif choice == 2:
        date = input('Enter date for check restuarant status(Mon-Sun): ')
        my_restuarant.open_resruarant(date)
    elif choice == 3:
        option = 1
        while option != 0:
            print('\n4, for show how many customers this restuarant has served.')
            print('5, for change to number_served attribute directly through an instance.')
            print('6, for change number_served attribute through method.')
            print('7, for adding the given value to number_served attribute.')
            print('0, for stop show and modify number served attribute.')
            option = int(input('Enter your options.'))
            if option == 4:
                print(f'My restuarant has served {my_restuarant.number_served} customers.')
            elif option == 5:
                new_num = int(input('Enter new number of customer that has served by this restuarant: '))
                my_restuarant.number_served = new_num
            elif option == 6:
                number_served = int(input('Enter number of customer this restuarant has served: '))
                my_restuarant.set_number_served(number_served)
            elif option == 7:
                additional_served = int(input('Enter number of customer you want to add to number_served: '))
                my_restuarant.increment_number_served(additional_served)
            elif option == 0:
                print('exit from modifying number served.')
            else:
                ('print invalid option!')
    elif choice == 0:
        print('Exiting program...')
    else:
        print('Invalid choice!')