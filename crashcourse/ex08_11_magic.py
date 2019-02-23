def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = magicians[i] + " the Great"
    return magicians

def show_magician(magicians):
    for magician in magicians:
        print(magician.title())

magicians = ['tim cooker', 'tang wei', 'xiaozi lan']
new_magicians = make_great(magicians[:])
show_magician(magicians)
show_magician(new_magicians)

