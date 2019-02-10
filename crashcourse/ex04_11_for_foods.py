my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
for food in my_foods:
    print(food)
print("\nMy firend's favorite foods are:")
for food in friend_foods:
    print(food)

my_foods.append('canoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)