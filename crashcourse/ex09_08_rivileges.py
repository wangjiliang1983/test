class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def descibe_user(self):
        print("The user name is: " + self.first_name.title() + " " + self.last_name.title() + ".")
    
    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name.title() + ".")
        print("Nice to meet you.")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():

    def __init__(self,privileages):
        self.privileages = privileages
    
    def show_privileages(self):
        print("The privileages are: ")
        for privileage in self.privileages:
            print("- " + privileage)


class Admin(User):

    def __init__(self, first_name, last_name, privileages):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileages)
    

admin_user = Admin('tom', 'jansen', ['can add post', 'can delete post', 'can ban user'])
admin_user.privileges.show_privileages()

