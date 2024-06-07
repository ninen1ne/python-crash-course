#This program receive customer order about t-shirt size and message they want to screen on it.
#19/3/2024




def make_shirt(size, message):
    """Describe size of shirt and tell customer."""
    print("We have recieve your order: " + size.title())
    print("and screen the following sentence: " + message)

#Call the function using positional arguments. (argument should type in ordered refer to definition of make_shirt function.)
make_shirt('l', 'I love Yuu')

#Call the function using keywork arguments.
make_shirt(message='I love Yuu', size='l')

