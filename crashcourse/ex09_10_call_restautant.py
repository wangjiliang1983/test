from ex09_10_restaurant import Restaurant

my_restaurant = Restaurant('Pizza hut', 'fast food')

my_restaurant.number_served = 23
print("The number of the restauant is: " + str(my_restaurant.number_served))
my_restaurant.set_number_served(34)
print("The number of the restauant is: " + str(my_restaurant.number_served))
my_restaurant.increment_number_served(34)
print("The number of the restauant is: " + str(my_restaurant.number_served))