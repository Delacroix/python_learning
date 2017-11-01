import json

init_num = raw_input("Input your favorite number: \n")
filename = 'num.json'
try:
    with open(filename, 'w') as f_obj:
        json.dump(init_num, f_obj)
except IOError:
    pass