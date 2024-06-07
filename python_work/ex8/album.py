def make_album(artist, title, number_of_tracks=''):
    """Build dictionary containing information about an album."""
    album_info = {
        'artist': artist,
        'title': title,
        }
    if number_of_tracks:
        album_info['number_of_tracks'] = number_of_tracks
    return album_info

album = make_album('taylor swift', 'fearless', 13)
print(album)
print("\n")

album = make_album('queen', 'news of the world',11)
print(album)
print("\n")

album = make_album('bon jovi', 'crush', number_of_tracks=11)
print(album)
print("\n")
