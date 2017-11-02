filename = 'guest.txt'

message = raw_input("Please enter your name:")

with open(filename, 'w') as file_object:
    file_object.write(message)