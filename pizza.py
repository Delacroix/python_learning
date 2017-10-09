def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

print("==================")


def make_pizza2(*toppings):
    print("\nMaking the pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
make_pizza2('pepperoni')
make_pizza2('mushrooms', 'green peppers', 'extra cheese')

print("==================")


def make_pizza3(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza3(16, 'pepperoni')
make_pizza3(12, 'mushrooms', 'green peppers', 'extra cheese')