# This program create function that recieve number of ingredients to made sandwiches for customer. :D
# 7/5/2024

""" 
    note: asterisk sign in the parameter *ingredients tell python to create tuple name ingredient 
    ans use it for store number of argument user has provide at function called section. 
"""
def make_sandwiches(*ingredients):
    """Collect the number of ingredients each person want in their sandwich."""
    if len(ingredients) == 1:
        print('\nSandwich still making with the following ingredient')
        print(f'- {ingredients[0]}')
    else:
        print('\nSandwich still making with the following ingredients')
        for ingredient in ingredients:
            print(f'- {ingredient}')

make_sandwiches('pork')
make_sandwiches('tomatoes', 'extra cheese', 'bun')
make_sandwiches('secret suace', 'bacon')