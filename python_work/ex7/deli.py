#this program assume that we have list of sandwiches_order after we made each sandwich we move it to another list called 
#finished_sandwiches at theendwe print out the sandwiches in the finished_sandwiches list.
#19/3/2024

sandwich_orders = ['vegan sandwich', 'chutney sandwich', 'falafel sandwich', 'italian sandwich']

finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print("\nI made " + finished_sandwich.title() + ".")
    finished_sandwiches.append(finished_sandwich)

print("\nThese order has been made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())