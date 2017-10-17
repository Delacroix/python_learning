class User():
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


user1 = User('Zilong', 'Yin')
user1.describe_user()
user1.greet_user()

user2 = User('Eitha', 'Chen')
user2.describe_user()
user2.greet_user()

user1.increment_login_attempts(5)
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)