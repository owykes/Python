def make_album(artist_name, album_title, song_name=None):
    album = {'artist': artist_name, 'album title': album_title}
    if song_name:
        album['song'] = song_name
    return album

while True:
    artist_name = input("Enter an artist name: ")
    album_title = input("Enter an album name: ")
    print(make_album(artist_name, album_title))
    check = input("type q to quit: ")
    if check == "q":
        break


