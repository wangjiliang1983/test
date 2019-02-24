
class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name.title() + ".")
        print("The restaurant cuisine is " + self.cuisine_type + ".")
    
    def open_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " is opening.")
    
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, number):
        self.number_served += number

my_restaurant = Restaurant('Pizza hut', 'fast food')

my_restaurant.number_served = 23
print("The number of the restauant is: " + str(my_restaurant.number_served))
my_restaurant.set_number_served(34)
print("The number of the restauant is: " + str(my_restaurant.number_served))
my_restaurant.increment_number_served(34)
print("The number of the restauant is: " + str(my_restaurant.number_served))