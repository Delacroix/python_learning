class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nRestaurant's name is " + self.restaurant_name.title())
        print("\nCuisine type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print("\nThe restaurant is open!")


restaurant = Restaurant('xiaoyu', 'hotpot')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant('laosichuan', 'chuan food')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant('yanjingmian', 'noodles')
restaurant3.describe_restaurant()
restaurant3.open_restaurant()