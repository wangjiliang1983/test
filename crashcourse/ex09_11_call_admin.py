from ex09_08_rivileges import Admin, User, Privileges

admin_user = Admin('tom', 'jansen', ['can add post', 'can delete post', 'can ban user'])
admin_user.privileges.show_privileages()