# 12/5/2024

file_path = '/Users/durandal/python_work/ex10/guest.txt'

with open(file_path) as file:
    guest_list = file.read()


while True:
    name = input('Dear customer please enter your name("q" for quit): ')
    if name == 'q':
        break
    guest_list += f'{name}\n'
    with open(file_path, 'w') as file:
        file.write(guest_list)
    print(f'Hi {name} you\'ve been added to the guess list book.')
