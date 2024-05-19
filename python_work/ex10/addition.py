# 13/5/2024
# Simple addition program but include exception.

print('This program adding 2 input')

try:
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
except ValueError:
    print('You can only type integer.')
else:
    sum = a + b
    print(f'Sum of {a} + {b} = {a+b}')