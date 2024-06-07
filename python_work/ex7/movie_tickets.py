#This program tell customer how much they will get charge depend on thier age.
#18/3/2024

#I think this program should use conditional test(if elif else loop)
print( "Welcome to theater customer!!!")
prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)

    if age < 3:
        print("  Your ticket is free!")
    elif age < 12:
        print("  Your ticket is $10 dollars")
    else:
        print("  Your ticket is $15 dollars")
        
#1) we input age as a string to compare with 'quit'
#2) then we convert age to integer to compare with another number in conditional test below.
#if user enter quit it will reach break statement
#tell python to stop the entire program lower than break
