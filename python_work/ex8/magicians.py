def show_magician(magicians):
    """Print each magician name from magicians list."""
    for magician in magicians:
        print("\nName of magician: " + magician.title())


magicians = ['monroe', 'lynnett', 'alpha']

show_magician(magicians)