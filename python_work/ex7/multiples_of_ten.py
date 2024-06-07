#We create program to tell user that number user has entered is multiple of 10 or not.
#3/18/2024


print("I will tell you that the number is multiple of 10 or not.")
number =  input("Enter your number: ")
number = int(number)

if number % 10 == 0:
    print("Your number is multiple of 10.")
else:
    print("Your number is not multiple of 10.")
