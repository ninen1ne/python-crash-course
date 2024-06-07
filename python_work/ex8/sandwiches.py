# This program create function that receive number of ingredients to made sandwiches for customer. c;
# 22/3/2024

# Note: The asterrisk in the parameter name *ingredients tell python to create empty tuple call ingredients.

def make_sandwich(*ingredients):
    """Collect a number of ingredients each person want in thier sandwich."""
    #Check if the list has only one item.
    if len(ingredients) == 1:
        print("\nSandwich still making with following ingredient:")
        print('- ' + ingredients[0])
    else:
         print("\nSandwich still making with following ingredients:")
         for ingredient in ingredients:
             print('- ' + ingredient)





make_sandwich('extra cheese')
make_sandwich('avocado', 'sausage', 'tomato')
make_sandwich('cucumber', 'cheese')