class Restaurant(object):
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("\nRestaurant's name is " + self.restaurant_name.title())
        print("Cuisine type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print("\nThe restaurant is open!")

    def read_number(self):
        print("\nThere are " + str(self.number_served) + " guests served.")

    def set_number_served(self, set_number):
        self.number_served = set_number

    def increment_number_served(self, guest_increment):
        self.number_served += guest_increment


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry', 'banana', 'chocolate']

    def guest_menu(self):
        print("We have these type of IceCream: ")
        for flavor in self.flavors:
            print(flavor.title())


guest_greetings = IceCreamStand('candy', 'snack')
guest_greetings.describe_restaurant()
guest_greetings.open_restaurant()
guest_greetings.guest_menu()
