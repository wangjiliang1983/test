from random import randint

class Die():
    
    def __init__(self, sides):
        self.sides = sides
    
    def roll_die(self):
        return randint(1,self.sides)

my_6die = Die(6)
for i in range(1,10):
    print(str(my_6die.roll_die()))

my_10die = Die(10)
for i in range(1,10):
    print(str(my_10die.roll_die()))

my_20die = Die(20)
for i in range(1,10):
    print(str(my_20die.roll_die()))