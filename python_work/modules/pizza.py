def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizzza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


