current_users = ['John', 'tom', 'admin', 'demo', 'Jerry']
new_users = ['Maria', 'TOM', 'Jack', 'DeMo', 'Lily']
user_is_new = 1
for user in new_users:
    user_is_new = 1
    for current_user in current_users:
        if user.lower() == current_user.lower():
            print("User name : " + user + " has been used. Please input another user name!")
            user_is_new = 0
    if user_is_new:
        print("Wellcome, " + user + ".")