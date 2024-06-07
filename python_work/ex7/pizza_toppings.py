prompt = "Enter your pizza toppings"
prompt += "\nOr if you not want anymore toppings enter 'quit': "

#My solution
active = True
while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print("Adding " +topping.title() + " to your pizza.")

#----------------------------------------------------------------------------------------
        
#Book solution 
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break      
