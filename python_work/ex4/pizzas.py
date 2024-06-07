# Defind my list of favorite pizzas.
pizzas = ['hawaiian pizza','pizza seafood','pizza pepperoni']
for pizza in pizzas:
    print(pizza.title() + "i really like it but i don't wanna eat it all week!")
print(f"tbh i don't really like pizza that much!")

# copy my list to friend_list.
friend_pizzas = pizzas[:]

# Add different new item for each list.
pizzas.append('neapolitan pizza')
friend_pizzas.append('sicilian pizza')

# Check that 2 list are separate.
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("\n")

print("My friend's favorite pizzas are:")
for f_pizza in friend_pizzas:
    print(f_pizza)
    