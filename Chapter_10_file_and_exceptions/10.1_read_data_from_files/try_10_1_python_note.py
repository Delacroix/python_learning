filename = 'learning_python.txt'
with open(filename) as file_object:
    content = file_object.read()
    print(content)


print("===========================")

with open(filename) as file_object2:
    for line in file_object2:
        print(line.rstrip())

print("===========================")

with open(filename) as file_object3:
    lines = file_object3.readlines()

for line in lines:
    print(line.rstrip())
