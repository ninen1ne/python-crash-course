#define our variables and lists.
number_0 = 71
number_1 = 27
mystery_number = 3
foods = ['pizza','spaghetti','steak','SALAD']
serial_numbers = ['001','002','003','004']
food_1 = 'soup'
food_2 = 'pizza'
food_3 = 'SALAD'

# contitional test process.
print(food_2 not in foods)
print('pizza' in foods)
print('Pizza' in foods)

if food_3 in foods:
    print(food_3.lower() + ", so fresh.")

print( number_0 >= 50 or number_1 == 26)
print( number_0 >= 50 and number_1 == 26)
print( number_0 >= 50 and number_1 != 26)