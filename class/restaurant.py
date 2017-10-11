class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nRestaurant's name is " + self.restaurant_name.title())
        print("\nCuisine type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print("\nThe restaurant is open!")

restaurant = Restaurant('shancheng', 'hotpot')
restaurant.describe_restaurant()
restaurant.open_restaurant()