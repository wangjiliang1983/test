car0 = 'Audi'
car1 = 'audi'
print(car0 == car1)
print(car0.title() == car1.title())
print(car0.lower() == car1.lower())

number0 = 35
number1 = 24
print(number0 == number1)
print(number0 != number1)
print(number0 > number1)
print(number0 < number1)
print(number0 >= number1)
print(number0 <= number1)

if number0 >30 and number1 < 25:
    print("Pass")
if number0 > 20 or number1 > 20:
    print("Pass")

a_list = ['Frank', 'Daivd', 'Xin', 'Ling']
employee = 'Frank'
if employee in a_list:
    print("Employee " + employee + " is in the company.")
employee = 'Fangze'
if employee not in a_list:
    print(employee + " is not employee of the company")