
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

person_names = ['sarah', 'cage', 'sink','phil']
for name in person_names:
    if name in favorite_languages.keys():
        print("Thanks " + name.title() + ", you are a great guy")
    else:
        print("Hi " + name.title() + ", please take a minute to finish the investigation")
    