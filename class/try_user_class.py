class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("\nUser's name is " + self.first_name + " " + self.last_name)

    def greet_user(self):
        print("\nGreetings! " + self.first_name + " " + self.last_name)

user1 = User('Zilong', 'Yin')
user1.describe_user()
user1.greet_user()

user2 = User('Eitha', 'Chen')
user2.describe_user()
user2.greet_user()