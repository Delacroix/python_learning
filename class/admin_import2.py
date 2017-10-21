from try_user_class import User
from user_module import Admin

test_admin = Admin('dx', 'lol')
test_admin.describe_user()
test_admin.privilege.show_privileges()

test2_admin = User('xxxx', 'yyyy')
test2_admin.describe_user()
test2_admin.greet_user()
