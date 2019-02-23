def make_car(brand, car_type, **car_info):
    car_profile = {}
    car_profile['brand_name'] = brand
    car_profile['type_name'] = car_type
    for key, value in car_info.items():
        car_profile[key] = value
    return car_profile

car = make_car('subaru', 'outback', color='blue',tow_package=True)
print(car)