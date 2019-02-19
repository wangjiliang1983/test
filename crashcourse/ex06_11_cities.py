cities = {
    'shanghai': {
        'country': 'china',
        'population': '25m',
        'fact': 'It is large',
    },
    'london': {
        'country': 'england',
        'population': '12m',
        'fact': 'It is small',
    },
    'tokyo': {
        'country': 'japan',
        'population': '35m',
        'fact': 'It is blue',
    },
}

for name, value in cities.items():
    print('City ' + name.title() + ':')
    for key, ff in value.items():
        print("\t" + key.title() + ": " + ff)
