def make_sandwich(*toppings):
    print("\n Making a sandwich with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_sandwich('chichken')
make_sandwich('eggs', 'mushrooms')
make_sandwich('eggs', 'mushrooms', 'hammer')


