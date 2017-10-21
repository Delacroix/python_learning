from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        result = randint(1, self.sides)
        print(result)


test = Die(6)
test.roll_die()
test.roll_die()
test.roll_die()
test.roll_die()
test.roll_die()
test.roll_die()
test.roll_die()

print("==========================")

test10 = Die(10)
test10.roll_die()
test10.roll_die()
test10.roll_die()
test10.roll_die()
test10.roll_die()
test10.roll_die()

print("==========================")

test20 = Die(20)
test20.roll_die()
test20.roll_die()
test20.roll_die()
test20.roll_die()
test20.roll_die()
test20.roll_die()
test20.roll_die()
test20.roll_die()
test20.roll_die()