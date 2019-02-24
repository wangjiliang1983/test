class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name.title() + ".")
        print("The restaurant cuisine is " + self.cuisine_type + ".")
    
    def open_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " is opening.")

my_restaurant = Restaurant('Pizza hut', 'fast food')
your_restaurant = Restaurant('KFC', 'fast food')
his_restaurant = Restaurant('Starbucks', 'coffee shop')
my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
his_restaurant.describe_restaurant()