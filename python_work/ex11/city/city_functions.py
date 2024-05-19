# 15/5/2024

def get_city_country(city, country, population=None):
    """Return neatly formetted about information of city and it country."""
    if population:
        info = f'{city.title()}, {country.title()} - population {population}'
    else:
        info = f'{city.title()}, {country.title()}'
    return info