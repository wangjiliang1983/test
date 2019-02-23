def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = magicians[i] + " the Great"

def show_magician(magicians):
    for magician in magicians:
        print(magician.title())

magicians = ['tim cooker', 'tang wei', 'xiaozi lan']
make_great(magicians)
show_magician(magicians)

