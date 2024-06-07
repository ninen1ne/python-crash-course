#This program receive customer order about t-shirt size and message they want to screen on it.
#19/3/2024


def make_shirt(size='large', message='I love Python'):
    """Describe size of shirt and tell customer."""
    print("We have recieve your order: " + size.title())
    print("and screen the following sentence: " + message)


#large shirt default message.
print("\nlarge shirt default message.")
make_shirt()

#medium shirt default message.
print("\nmedium shirt default message.")
make_shirt(size='medium')

#shirt with any size any message.
print("\nshirt with any size any message.")
make_shirt('small', 'I love Yuu')
print('\n')
make_shirt(size='small', message='I love Yuu')