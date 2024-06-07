
# 22/3/2024

def make_car(manufacturer, model, **car_info):
    """receive information of car and store in dictionary"""
    
    # create empty list hold value.
    car_profile = {}
    car_profile['manufacturer'] = manufacturer.title()
    car_profile['model'] = model.title()

    for key, value in car_info.items():
        car_profile[key] = value
    return car_profile

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_volkswagen = make_car('volkswagen group', 'virtus', color='red', year=2018)
print(my_volkswagen)