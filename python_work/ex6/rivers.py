nationality_rivers = {
    'danube': 'Germany, Austria, Slovakia, Hungary, Croatia, Serbia, Romania, Bulgaria, Moldova and Ukraine.',
    'amur': 'China, Mongolia and Russia',
    'rhine': 'Switzerland, Austria, Germany, France, Netherlands, Principality of Liechtenstein.',
    }
about_rivers = {
    'danube': 'The Danube is the second-longest river in Europe, after the Volga in Russia.\n' +
    'It flows through Central and Southeastern Europe, from the Black Forest south into the\n' +
    'Black Sea. A large and historically important river, it was once a frontier of the Roman Empire',
    'amur': 'The Amur River or Heilong River is a perennial river in Northeast Asia, forming the natural border between the Russian Far East and Northeast China.',
    'rhine': 'The Rhine is one of the major European rivers. The river begins in the Swiss canton of Graubünden in the southeastern Swiss Alps.',
    }

#show sentence about each river.
for river in nationality_rivers.keys():
    print('\n' + river.title() + ': ' + about_rivers[river])

#show name of rivers and show how many country that each river passes by.
for river, country in nationality_rivers.items():
    print('\n' + river.title() + ': ' + 'this river has passes many countries include--> ' + country)
