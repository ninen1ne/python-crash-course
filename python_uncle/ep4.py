
# 30/3/2024
friends = ['nine', 'kung', 'tor']
print(type(friends))

print(friends[0])
print(friends[1])
print(friends[2])
print(friends)

pets = ('cat', 'dog')
print(type(pets))
del friends[0]
print(friends)
friends.remove('tor')
print(friends)

friends.append('yolle')
friends.append('yuu')
print(friends)

last_friend = friends.pop()
print(last_friend)

friends.insert(1, 'pokemon')
print(friends)

friends[2] = 'pun'
print(friends)

friends.insert(1, friends.pop(2))
print(friends)

for friend in friends:
    print(friend)

for i, friend in enumerate(friends):
    print(i, friend)

for i, friend in enumerate(friends, start=1):
    print(i, friend)

#---------------------------------------------------------------------------------------------------
# solution-1
thaichar = []

for i in range(3585, 3631):
    alphabet = chr(i)
    if alphabet == 'ฤ':
        continue
    elif alphabet == 'ฦ':
        continue
    else:
        thaichar.append(alphabet)


print(thaichar)
print(f'พยัญชนะไทยมี: {str(len(thaichar))} ตัว')

# Solution-2 
# But i think this solution is faster than the frist solution(maybe) because we don't have to loop through all condition several times.

thaichar = []

for i in range(3585, 3631):
    alphabet = chr(i)
    thaichar.append(alphabet)

thaichar.remove('ฤ')
thaichar.remove('ฦ')

print(thaichar)
print(f'พยัญชนะไทยมี: {str(len(thaichar))} ตัว')

# Check index of item in side list. 
print(thaichar.index('ร'))