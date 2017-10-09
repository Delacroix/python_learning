def show_magicians(init_names):
    for name in init_names:
        print(name)

def make_great(init_names, final_names):
    while init_names:
        current_name = init_names.pop()
        print(current_name + " the Great")
        final_names.append(current_name + " the Great")


init_names = ['magician_a', 'magician_b', 'magician_c']
final_names = []
make_great(init_names[:], final_names)
show_magicians(init_names)
show_magicians(final_names)