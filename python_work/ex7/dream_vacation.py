# This program recieve name and users dream vacation location and store in dictionary called responses and show the result at the edn of program. :D
# 19/3/2024

responses ={}

polling_active = True

while polling_active:
    name = input("Enter your name: ")
    dream_vacation = input("Where would you like to go at least once upon a time?: ")


    responses[name] = dream_vacation

    order = input("would you like to end the poll (yes/no): ")
    if order == 'yes':
        polling_active = False

print("\n")
print("------------------------------The result of this poll----------------------------------")

for name, response in responses.items():
    print(name.title() + " like to go to " + response.title() + ".")



