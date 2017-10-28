filename = 'why_python.txt'

message = ''

while message != 'quit':
    message = raw_input("Why python?")
    if message != 'quit':
        with open(filename, 'a') as file_object:
            file_object.write(message + "\n")
    else:
        break

