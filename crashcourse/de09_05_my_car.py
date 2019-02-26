import de09_04_car 

my_new_car = de09_04_car.Car('audo', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_beetle = de09_04_car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = de09_04_car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())