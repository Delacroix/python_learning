def greet_user():
    """print easy greet"""
    print('hello')
greet_user()
print("===============")
def greet_user2(username):
    print("Hello, " + username.title() + "!")
greet_user2('jessie')
print("================")
def display_message():
    print("I'm learning def")
display_message()
print("===============")


def favorite_book(title):
    print("One of my favorite books is " + title.title())
favorite_book('Alice in wonderland')
print("=====================")


def describe_pet(annimal_type, pet_name):
    """display pets information"""
    print("\nI have a " + annimal_type + ".")
    print("My " + annimal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(annimal_type='cat', pet_name='molly')
print("=================")


def describe_pets(pet_name, animal_type='dog'):
    """display pets info"""
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pets('edgar')
describe_pets('harry', 'hamster')
describe_pets('willie')
describe_pets(pet_name='willie')
describe_pets('harry', 'hamster')
describe_pets(pet_name='harry', animal_type='hamster')
describe_pets(animal_type='hamster', pet_name='harry')