vacation_locs = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    location = input("If you could visit one place in the world, where would you go?")
    vacation_locs[name] = location

    ans = input("Would you let another person to do the polling? (yes / no):")
    if ans == 'no':
        polling_active = False

for name, loc in vacation_locs.items():
    print(name.title() + " would like to visit " + loc + ".")
