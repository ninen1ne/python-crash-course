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

album = make_album('Taylor Swift', 'Fearless', 13)
print(album)

album = make_album('Westlife', 'Coast to Coast')
print(album)

album = make_album('Taylor Swift', '1989(Taylor\'s Version)')
print(album)