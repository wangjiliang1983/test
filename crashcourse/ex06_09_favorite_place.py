favorite_places = {
    'Frank': ['she hill', 'huangpu river', 'yangzi river'],
    'Ling': ['emei hill', 'hainan island', 'dead lake'],
    'Xin': ['changbai hill', 'daxingan forest', 'beidai river'],
}

for name, places in favorite_places.items():
    place_int = ''
    for place in places[:-1]:
        place_int = place_int + place.title() + ', '
    place_int = place_int + 'and ' + places[-1].title() + '.'
    print(name.title() + " likes to go to " + place_int)
