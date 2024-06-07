# This program receive city and it country from user and combine them togehter to get variable info and show to user.
#20/3/2024




def city_country(city, country):
    """Describe city and where it's country"""
    location = city + ", " + country
    return location.title()


info = city_country('bangkok', 'thailand')
print(info)

info = city_country('berlin', 'germany')
print(info)

info = city_country('paris', 'france')
print(info)

