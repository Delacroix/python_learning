class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("\nRestaurant's name is " + self.restaurant_name.title())
        print("\nCuisine type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print("\nThe restaurant is open!")

    def read_number(self):
        print("\nThere are " + str(self.number_served) + " guests served.")

    def set_number_served(self, set_number):
        self.number_served = set_number

    def increment_number_served(self, guest_increment):
        self.number_served += guest_increment


restaurant = Restaurant('xiaoyu', 'hotpot')
restaurant.set_number_served(100)

restaurant.describe_restaurant()
restaurant.read_number()
restaurant.increment_number_served(20)
restaurant.describe_restaurant()
restaurant.read_number()


