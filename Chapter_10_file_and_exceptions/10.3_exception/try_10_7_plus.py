print("Enter 2 numbers to make a plus.")
print("Enter 'q' to exit.\n")

while True:
    try:
        num1 = raw_input("Number 1: \n")
        if num1 == 'q':
            break
        num2 = raw_input("Number 2: \n")
        if num2 == 'q':
            break
        result = int(num1) + int(num2)
        print("The result is " + str(result))

    except ValueError:
        print("You can only enter numbers.")
