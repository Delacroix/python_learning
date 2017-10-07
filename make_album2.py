def make_album(music_name, album_name):
    music_info = {'music': music_name, 'album': album_name}
    return music_info

while True:
    m_name = raw_input("\nPlease input your music name: ")
    print("\nEnter 'q' at any time to quit")
    if m_name == 'q':
        break
    a_name = raw_input("\nPlease input your album name: ")
    print("\nEnter 'q' at any time to quit")
    if a_name == 'q':
        break
    music_infomation = make_album(m_name, a_name)
    print("\nAlbum info: ")
    print(music_infomation)