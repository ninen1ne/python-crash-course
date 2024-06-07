favorite_languages = {
    'nine': 'python',
    'aom': 'python',
    'park': 'c',
    'tack': 'c++',
    'yuu': 'java',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + '.')


users = ['nine','tor','kung','poom','park','pun','tack','yoll','yuu','theta','aom','thor','thanawat','delta']

for user in users:
    if user in favorite_languages.keys():
        print('\n' + user.title() + ',' + 'Thanks for polling.')
    else:
        print('\n' + user.title() + ', ' "Please take the poll.")

