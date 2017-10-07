def make_album(music_name, album_name, count = ''):
    if count:
        music = {'music': music_name, 'album': album_name, 'count': count}
        return music
    else:
        music = {'music': music_name, 'album': album_name}
        return music
music1 = make_album('music1', 'album1', '10')
print(music1)
music2 = make_album('music2', 'album2')
print(music2)

