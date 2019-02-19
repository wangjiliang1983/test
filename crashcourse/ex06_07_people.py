people = {
    'person1': {'first_name': 'Frank',
                'last_name': 'Zhao,',
                'age': 42,
                'city': 'Shanghai',
                },
    'person2': {'first_name' : 'Ling',
                'last_name': 'Ling',
                'age': 33,
                'city': 'Shanghai',
                },
    'person3': {'first_name': 'Xin',
                'last_name': 'Zhang',
                'age': 34,
                'city': 'Shanghai',
    },
}

for key, value in people.items():
    print(key + ":")
    print(value['first_name'].title() + " " + value['last_name'].title()
        + " is located in " + value['city'] + ". He/She is " + str(value['age']) + " years old.")


