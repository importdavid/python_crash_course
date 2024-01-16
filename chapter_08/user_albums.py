# 8-8. User Albums: pg 142
# MODIFIES 8-7. Album: pg 142

def make_album(artist, title, num_songs=None):
    album = {}
    if num_songs: album['tracks'] = num_songs
    album['artist'] = artist
    album['title'] = title
    return album

while True:
    artist = input("Provide artist's name:\n")
    title = input("Provide album title:\n")
    print(make_album(artist, title))
    more = input('Another? ("q" to quit)\n')
    if more == 'q': break
albums = []

albums.append(make_album('Jukebox the Ghost', 'Everything Under the Sun'))
albums.append(make_album('Sara Bareilles', 'Kaleidoscope Heart'))
albums.append(make_album('Jack Johnson', 'In Between Dreams', 14))

print(albums)