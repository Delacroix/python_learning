class User(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("\nUser's name is " + self.first_name + " " + self.last_name)

    def greet_user(self):
        print("\nGreetings! " + self.first_name + " " + self.last_name)

    def increment_login_attempts(self, increment_login):
        self.login_attempts += increment_login

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name):
        super(Admin, self).__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post',
                           'can ban user']

    def show_privileges(self):
        print("As an admin, you have these privileges below: ")
        for privilege in self.privileges:
            print(privilege.title())


administrator = Admin('Zilong', 'Yin')
administrator.describe_user()
administrator.greet_user()
administrator.show_privileges()
