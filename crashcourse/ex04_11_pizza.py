favorite_pizza = ['Papa Johns', 'KFC', 'pepperoni pizza']
for pizza in favorite_pizza:
    print("I like " + pizza)
print("I really love pizza!")

friend_pizzas = favorite_pizza[:]
favorite_pizza.append('hailumanyi')
friend_pizzas.append('xiaren')

print("My favorite pizzas are:")
for pizza in favorite_pizza:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
