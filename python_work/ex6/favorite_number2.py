'''This program retrieve dictionary about person and thier favorite number and then display person name and thier favorite numbers!!!
1) one person can have more than 1 favorite number that why we use list nested inside dictionary.

'''

#create a dictionary key is name of each person and value is a list of each person favorite numbers.
favorite_number = {
    'nine': [7,28,69,777],
    'tor': [100,1,20],
    'feaung': [69],
    'kung': [5,27],
    'pun': [10,36],
}

#1) we loop through dictionary and use person variable for hold key(name) and use variable name numbers for hold a list of each person favorite number. 
for person, numbers in favorite_number.items():
    #check if person has more than one favorite number.
    if len(numbers) > 1:
        print('\n' + person.title() + "'s favorite numbers are:")
        for number in numbers:
            print(number)
    #check in condition that person has only one favorite number. 
    elif len(numbers) == 1:
        print('\n' + person.title() + "'s favorite number is:")
        for number in numbers:
            print(number)