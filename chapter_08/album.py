# 8-7. Album: pg 142

def make_album(artist, title, num_songs=None):
    album = {}
    if num_songs: album['tracks'] = num_songs
    album['artist'] = artist
    album['title'] = title
    return album

albums = []

albums.append(make_album('Jukebox the Ghost', 'Everything Under the Sun'))
albums.append(make_album('Sara Bareilles', 'Kaleidoscope Heart'))
albums.append(make_album('Jack Johnson', 'In Between Dreams', 14))

print(albums)