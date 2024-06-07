
sandwich_orders = ['vegan sandwich', 'pastrami', 'chutney sandwich', 'falafel sandwich','pastrami', 'italian sandwich', 'pastrami']

finished_sandwiches = []
print("The deli has run out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print("\nI made " + finished_sandwich.title() + ".")
    finished_sandwiches.append(finished_sandwich)

print("\nThese order has been made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())