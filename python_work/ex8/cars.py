def make_car(manufacturer, model, **other_info):
    """Describe a car in a simple term. :D"""
    car_profile = {}
    car_profile['manufacturer'] = manufacturer
    car_profile['model'] = model
    for key, value in other_info.items():
        car_profile[key] = value

    return car_profile

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

car = make_car('honda', 'accord', year=1991, color='white',headlights='popup')
print(car)