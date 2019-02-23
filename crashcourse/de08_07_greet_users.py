def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        meg = "Hello, " + name.title() + "!"

username = ['hannah', 'ty', 'margot']
greet_users(username)