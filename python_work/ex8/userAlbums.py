# 6/5/2024
def make_album(artist, title, numberOfTrack=None):
    """return a information about album."""
    album = {
        'artist': artist,
        'title': title,
    }
    if numberOfTrack:
        album['numberOfTrack'] = numberOfTrack
    return album

while True:
    print('\nEnter your favorite artist and their album title.')
    print('Type "q" at any time for quit program')

    artist = input('Artist name: ')
    if artist == 'q':
        break
    title = input('album name: ')
    if title == 'q':
        break
    
    albumInfo = make_album(artist, title)
    print(f'Album information: {albumInfo}')