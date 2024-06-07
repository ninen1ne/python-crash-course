cities = {
    'Barcelona': {
        'country': 'spain',
        'population': '1.6 M',
        'fact': 'Spain and Portuguese made the Treaty of Tordesillas.',
    },
    'tokyo': {
        'country': 'japan',
        'population': '14 M',
        'fact': 'Japan has 110 active volcanoes.',
    },
    'bangkok': {
        'country': 'thailand',
        'population': '8.3 M',
        'fact': 'Thailand is actually the same size as France.',
    },
    }

for city, city_info in cities.items():
    print('\n' + city.title() +':')
    print('This city located at: ' + city_info['country'].title())
    print('Approximate population: ' + city_info['population'])
    print('Fact about this country: ' + city_info['fact'])