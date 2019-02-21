def city_country(city,country):
    c_country = city + ', ' + country
    return c_country.title()

message = city_country('santiago','chile')
print('"' + message + '"')
    