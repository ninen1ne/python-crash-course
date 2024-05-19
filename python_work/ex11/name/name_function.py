# 15/5/2024

def get_formatted_name(first, last, middle=''):
    """Return neatly formatted full name."""
    if middle:
        full_name = f'{first} {middle} {last}'
    else:
        full_name = f'{first} {last}'
    return full_name.title()

