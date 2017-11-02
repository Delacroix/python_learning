filename = 'guest_book.txt'

message = ""

while message != 'quit':
    message = raw_input("Please enter your name:\n")
    print("Greetings, " + message)
    with open(filename, 'a') as file_object:
        file_object.write(message + "\n")
