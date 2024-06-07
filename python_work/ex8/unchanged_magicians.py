
#22/3/2024

def show_magician(magicians):
    """Print each magician name from magicians list."""
    for magician in magicians:
        print(magician.title())



def make_great(magicians):
    """Adding phrase in front of magicians name."""
    # Build a new list to hold the great magicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + " the Great"
        great_magicians.append(great_magician)

    # Add the great magicians back to magicians list.
    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians

magicians = ['Harry Hodini', 'David Blaine', 'Teller']
show_magician(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magician(great_magicians)

print("\nOriginal magicians:")
show_magician(magicians)
