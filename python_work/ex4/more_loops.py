my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
i = 0
j = 0 
print("My favorite food are:")
for food in my_foods:
    print(my_foods[i])
    i = i + 1

print("\nMy friend's favorite food are:")
for food in friend_foods:
    print(friend_foods[j])
    j = j + 1 

# another solution i turned my_food variable to str then plug in my_foods method :D
for my_food in range(0,3):
    print(my_foods[my_food])