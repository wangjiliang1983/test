sandwich_orders = ['chicken', 'fish', 'pastrami', 'burger']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    if order =='pastrami':
        print("Sorry, pastrami sandwiches have been sold out!")
    else:
        print("I made your " + order + " sandwich.")
        finished_sandwiches.append(order)

for sandwich in finished_sandwiches:
    print(sandwich)