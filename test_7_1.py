car_rent = raw_input("What kind of car do you want? ")
print("\nLet me see if I can find you a " + car_rent + ".")

print("===========================")
booking_seats = raw_input("How many people will you take? ")
if int(booking_seats) > 8:
    print("There's no empty table.")
else:
    print("There is an empty table.")

print("============================")
ten_multi = raw_input("Please input a number: ")
if int(ten_multi) % 10 == 0:
    print("It's multi-ten")
else:
    print("It isn't multi-ten")