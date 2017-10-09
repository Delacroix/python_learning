def make_sandwich(*toppings):
    print("\nMaking the sandwich with following toppings:")
    for topping in toppings:
        print("- " + topping)

make_sandwich('pepper')
make_sandwich('coco', 'butter')
make_sandwich('fruit', 'beef', 'onion')