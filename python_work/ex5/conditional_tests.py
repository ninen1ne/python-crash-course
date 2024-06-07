'''This is a 10 conditional test program'''

age_0 = 20
age_1 = 35
dangerous_animals = ['wolf','lion','fox','crocodile','snake']
animal_0 = 'dog'
animal_1 = 'cat'
animal_2 = 'wolf'
animal_3 = dangerous_animals[3]
answer = 47

if animal_3 in dangerous_animals[2]: # check if animal_3 is in the 4th position in the list it will return trun else it will return False.
    print('Danger')
else:
    print('danger aswell')

print('wolf' in dangerous_animals) # wolf is in dangerous_animals list it's then return True.

print('dog'  in dangerous_animals) # dog is not in dangerous_animals list python then return False.

if answer == 28:
    print('that correct!!!') #if answer equal 28 return true else return false.
else:
    print('wrong!')

print(age_0 >= 20 and age_1 <= 10) #if both conditrional test passes it return true.

print(age_0 == 21 or age_1 == 36) # if either or both conditional test passes it reture ture.

if animal_0 not in dangerous_animals:
    print(animal_0.title() + ", this animal is considered safe for human.")

if animal_2 in dangerous_animals:
    print(animal_2.upper() + ", get away from this area!!!")

if animal_1 in dangerous_animals:
    print('Dangerous')
else:
    print(animal_1.title() + ", it's safe.")

if animal_3 in dangerous_animals:
    print("I love U")