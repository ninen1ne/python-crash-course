#lesson about nesting dictionary in side a list.
#first create dictionary contain information about each person.
person_0 = {
    'first_name': 'norawee',
    'last_name': 'laohateerapong',
    'age': 17,
    'city': 'nonthaburi',
}

person_1 = {
    'first_name': 'issaret',
    'last_name': 'kraibun',
    'age': 17,
    'city': 'nonthaburi',
}


person_2 = {
    'first_name': 'mojo',
    'last_name': 'jojo',
    'age': 170,
    'city': 'polatch',
}

#second create list for contain each person dictionary.
people = [person_0, person_1, person_2]

#3) loop through the list of people to accessing each dictionary inside a list by use it key.
for user in people:
    full_name = user['first_name'] + ' ' + user['last_name']
    age = user['age']
    location = user['city']
#4) show the output about information we know for each person. ;)
    print('full name: ' + full_name.title())
    print('age: ' + str(age) + ' years old')
    print('location: ' + location.title() + '\n')

print("-------------------------------------------------End------------------------------------------------")

