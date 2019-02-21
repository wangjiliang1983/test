def describe_pet(animal_type='dog', pet_name='peter'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(pet_name='willie')