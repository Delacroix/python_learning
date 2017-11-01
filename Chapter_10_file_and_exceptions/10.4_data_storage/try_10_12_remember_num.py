import json


def get_stored_number():
    filename = 'num_3.json'
    try:
        with open(filename) as f_obj:
            num = json.load(f_obj)
    except IOError:
        return None
    else:
        return num


def get_new_num():
    num = raw_input("What's your favorite number?\n")
    filename = 'num_3.json'
    with open(filename, 'w') as f_obj:
        json.dump(num, f_obj)
    return num

def tell_user():
    num = get_stored_number()
    if num:
        print("Your favorite number was " + num + ", am I right?")
    else:
        num = get_stored_number()
        print("You can tell me your favorite number!")

tell_user()