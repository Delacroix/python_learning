def get_famatted_name(first_name, last_name):
    """return tidy name"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

#this is a infinite cycle
while True:
    print("\nPlease tell me your name: ")
    f_name = raw_input("First name: ")
    l_name = raw_input("Last name: ")

    formatted_name = get_famatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")