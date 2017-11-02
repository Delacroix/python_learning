from car_module import Car

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        if self.battery_size == 70:
            total_range = 240
        elif self.battery_size == 85:
            total_range = 270

        message = "This car can go approximately " + str(total_range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()