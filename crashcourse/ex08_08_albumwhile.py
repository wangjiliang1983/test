def make_album(singer, album):
    album_dict = {'singer': singer, 'album': album}
    return album_dict

while True:
    print("\nPlease give me the singer name and album name:")
    print("(Enter 'q' to quit)")

    singer = input("Please enter the singer name: ")
    if singer == 'q':
        break
    album = input("Please enter album name: ")
    if album == 'q':
        break
    album_dict = make_album(singer,album)
    print(album_dict)