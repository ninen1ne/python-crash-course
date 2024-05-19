# 13/5/2024
# using while loop receive number from user if user input is str enter text instead of number.
Sum = 0
while True:
    try:
        x = input('Enter first number("q" for quit): ')
        if x == 'q':
            break
        x = int(x)

        y = input('Enter second number("q" for quit): ')
        if y == 'q':
            break
        y = int(y)

    except ValueError:
        print('Sorry I only need integer.')
    else:
        Sum = x + y
        print(f'\nresult = {Sum}')