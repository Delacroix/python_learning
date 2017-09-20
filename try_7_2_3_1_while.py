prompt = "\nHow old are you?"
prompt += "\nPlease enter your age, or to end session please enter 'quit': "
while True:
    age = raw_input(prompt)
    if age == 'quit':
        break
    elif int(age) < 3:
        print("It's free for you.")
    elif int(age) <= 12:
        print("You have to pay $10.")
    else:
        print("You have to pay $15.")
