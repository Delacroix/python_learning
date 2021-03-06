import json


def get_stored_username():
    """If username was stored, then fetch it."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except IOError:
        return None
    else:
        return username


def get_new_username():
    username = raw_input("You haven't registered yet, what is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Edited for try_10_13_user_check"""
    username = raw_input("Please input your username: \n")
    # username = get_stored_username()
    # if username:
    if username == get_stored_username():
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
