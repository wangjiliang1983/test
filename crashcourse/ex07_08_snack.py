sandwich_orders = ['chicken', 'fish', 'burger']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print("I made your " + order + " sandwich.")
    finished_sandwiches.append(order)

for sandwich in finished_sandwiches:
    print(sandwich)