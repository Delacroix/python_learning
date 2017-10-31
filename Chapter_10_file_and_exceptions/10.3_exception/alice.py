filename = 'alice1.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except IOError:
    msg = "Sorry, the file" + filename + " does not exist."
    print(msg)