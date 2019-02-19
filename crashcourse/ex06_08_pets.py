kitty = {'catigory': 'yingduan', 'host': 'Frank',}
doggy = {'catigory': 'muyang', 'host': 'Xin',}
piggy = {'catigory': 'yezhu', 'host': 'Ling',}

pets = [kitty, doggy, piggy]

for animal in pets:
    print(animal['catigory'].title() + " belongs to " + animal['host'].title())
