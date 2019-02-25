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

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def describe_flavors(self):
        print("Here are the flavors:")
        for flavor in self.flavors:
            print("- " + flavor.title())
        
flavors = ['Chocolate', 'vanila', 'stewberry', 'blue berry']
my_icecreamshop = IceCreamStand('cold stone', 'icecream', flavors)
my_icecreamshop.describe_flavors()