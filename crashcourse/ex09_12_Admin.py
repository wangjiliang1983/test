from ex09_12_user import User

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
    
