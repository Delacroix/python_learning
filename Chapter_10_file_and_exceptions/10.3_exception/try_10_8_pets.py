file_1 = 'cats.txt'
file_2 = 'dogs.txt'

try:
    with open(file_1) as f_obj_1:
        content = f_obj_1.read()
        print(content)
    with open(file_2) as f_obj_2:
        content2 = f_obj_2.read()
        print(content2)
except IOError:
    #print("File " + file_2 + " not found.")
    pass