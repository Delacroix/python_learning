with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)


print("================")
file_name = 'pi_digits2.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line)

print("================")
file_name = 'pi_digits3.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())