dog = {
    'name': 'cookie',
    'animal type': 'dog',
    'type': 'mammal',
    'owner': 'nine',
    'color': 'black',
    'age': 7,
    
}

cat = {
    'name': 'gege',
    'animal type': 'cat',
    'type': 'mammal',
    'owner': 'kung',
    'color': 'orange',
    'age': 10
}

turtle = {
    'name': 'pa',
    'animal type': 'turtle',
    'type': 'reptile',
    'owner': 'flueng',
    'color': ' dark-green',
    'age': 0.4
}


pets = [dog, cat, turtle]

for pet in pets:
    print('Information about: ' + pet['name'].title())
    for key, value in pet.items():
        if key == 'age':
            print(key + ', ' +str(value) + ' years old')
        elif key != 'age':
            print(key + ', ' + value)
    print('\n') 

