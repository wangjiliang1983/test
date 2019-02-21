def make_album(singer, album):
    album_dict = {'singer': singer, 'album': album}
    return album_dict

album1 = make_album('Alice', 'alice new')
album2 = make_album('king', 'let it go')
album3 = make_album('Queen', 'slicely')

print(album1)
print(album2)
print(album3)
