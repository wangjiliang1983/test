
from ex09_12_Admin import Admin, Privileges

admin_user = Admin('tom', 'jansen', ['can add post', 'can delete post', 'can ban user'])
admin_user.privileges.show_privileages()