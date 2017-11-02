try:
    num1 = raw_input("Number 1:\n")
    num2 = raw_input("Number 2:\n")
    result = int(num1) + int(num2)
except ValueError:
    print("Make sure you type in numbers.")
else:
    print("Number 1 plus Number 2 equals to: " + str(result))
