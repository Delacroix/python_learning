prompt = "\nEnter something you want to add to pizza:"
prompt += "\nEnter 'quit' to finish."
while True:
    pizza = raw_input(prompt)
    if pizza == 'quit':
        break
    print("\nYou added " + pizza.title() + " to the pizza!")
