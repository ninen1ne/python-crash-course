def make_album(artist, title, track=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if track:
        album_dict['track'] = track
    return album_dict

# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know thow to quit.
print("Enter 'quit' at any time to stop.")


while True:
    title = input(title_prompt)
    if title == 'q':
        break

    artist = input(artist_prompt)
    if artist == 'q':
        break

    album = make_album(artist, title)
    print(album)


print("\nThanks for responding!")



