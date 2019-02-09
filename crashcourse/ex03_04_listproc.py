print("This is Ex3-4")
friends_name = ['Xin Zhang', 'David Wang', 'Ling Ling']
print(friends_name)

print("\n")
print("This is Ex3-5")
can_not_att_name = 'Xin Zhang'
print(can_not_att_name + " can not attand the dinner!")
friends_name.remove(can_not_att_name)
print(friends_name)

print("\n")
print("This is Ex3-6")
print("We have found a bigger table!")
friends_name.insert(0,'Frank Zhao')
friends_name.insert(1,'Xiao Qiao')
friends_name.append('Weiguo Zhang')
print(friends_name)

print("\n")
print("This is Ex3-7")
print("Sorry. We can only invite two persons to dinner.")
can_not_att_name = friends_name.pop()
print('Sorry ' + can_not_att_name.title() + ', we can not invite you to dinner.')
can_not_att_name = friends_name.pop()
print('Sorry ' + can_not_att_name.title() + ', we can not invite you to dinner.')
can_not_att_name = friends_name.pop()
print('Sorry ' + can_not_att_name.title() + ', we can not invite you to dinner.')

print('Hi ' + friends_name[0] + ', welcome to the dinner!')
print('Hi ' + friends_name[1] + ', welcome to the dinner!')

del friends_name[0]
del friends_name[0]
print(friends_name)