class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def descibe_user(self):
        print("The user name is: " + self.first_name.title() + " " + self.last_name.title() + ".")
    
    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name.title() + ".")
        print("Nice to meet you.")

user_00 = User('Frank', 'Zhao')
user_01 = User('Ling', 'Ling')
user_02 = User('David', 'Wang')

user_01.descibe_user()
user_01.greet_user()
user_02.descibe_user()
user_02.greet_user()
user_00.descibe_user()
user_00.greet_user()