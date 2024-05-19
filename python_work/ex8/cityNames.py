# 6/5/2024
def city_country(city, country):
    """Return formatted of city and it country."""
    message = f'{city}, {country}'
    return message.title()

location = city_country('Berlin', 'Germany')
print(location)

location = city_country('Moscow', 'Russia')
print(location)

location = city_country('London', 'United Kingdom')
print(location)