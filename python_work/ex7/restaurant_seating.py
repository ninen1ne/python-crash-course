guess_count =input('How many people in your dinner group: ')
guess_count= int(guess_count)

if guess_count > 8:
    print("My customer you'll have to wait for a table.")
else:
    print("A table is available now.")