favorite_number = {
    'xin': [12, 11, 10],
    'frank': [22, 24, 19],
    'ling': [35, 31, 39],
}

for name,value in favorite_number.items():
    num_str = ''
    for num in value[:-1]:
        num_str = num_str + str(num) + ', '
    num_str = num_str + 'and ' + str(num) + '.'
    print(name.title() + "'s favorite numbers are " + num_str)