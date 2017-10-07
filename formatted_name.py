def get_formatted_name(first_name, last_name):
    """:return tidy names"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

print('===========')


def get_formatted_name2(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
musician2 = get_formatted_name2('john', 'lee', 'hooker')
print(musician2)

print('===========')


def get_formatted_name3(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician3 = get_formatted_name3('jimi', 'hendrix')
musician33 = get_formatted_name3('john', 'lee', 'hooker')
print(musician3)
print(musician33)