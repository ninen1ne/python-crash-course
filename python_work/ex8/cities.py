#create function that receive input of user and response back is form of sentence such as Yolle is in France.
#19/3/2024

def describe_city(name, country='thailand'):
    """"""
    message = name.title() + " is in " + country.title() + '.'
    print(message)
    
describe_city('bangkok')
describe_city(name='nonthaburi')
describe_city(name='berlin', country='germany')

