favorite_places = {
    'nine': ['place that i will be with yuu.', 'venice', 'everest'],
    'john': ['banff national park', 'machu picchu', 'marrakesh'],
    'feyd': ['dune', 'jordan', 'sossusvlei'],
    }

for person, places in favorite_places.items():
    print('\n' + person.title() + "'s favorite places is: ")
    for place in places:
        print(place.title())
