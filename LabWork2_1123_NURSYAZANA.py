'''
    Program purpose: To designing a hotel reservation system where guests can book rooms online.
    Programmer: NURSYAZANA BINTI MOHAMAD NOH EZAM
    Date: 23 February 2024
'''
print ("\n")
print("Welcome to DiNara Hotel Reservation System")
print ("\n")
#Display Room Types
print("DiNara Hotel Room Type:")
print("1.Single: RM100 per night")
print("2.Double: RM150 per night")
print("3.Suite: RM250 per night")
print ("\n")
#Prompt user to input number to choose room type
type_room = int(input("Enter your room (Choose number): "))
#Prompt user to input per night
per_night = int(input("Enter your per night:"))
#Prompt user to input number of room
num_room = int(input("Enter you number of room:"))

single_room = 100
double_room = 150
suite_room = 250

#Error if user input invalid number
if type_room not in [1, 2, 3]:
    print("Error: Invalid option number of room. Please try again !")
if num_room <= 0 or per_night <= 0:
    print("Error: Number of rooms and nights must be positive.")


if type_room == 1: #To calculate the Single Room
    total = single_room * per_night * num_room
    print(f"Total price (RM) : {total:.2f}")
    if per_night > 7:
        print("Awesome! You get a free breakfast voucher.")
elif type_room == 2: #To calculate the Double Room
    total = double_room * per_night * num_room
    print(f"Total price (RM) : {total:.2f}")
elif type_room == 3: #To calculate the Suite Room
    total = suite_room * per_night * num_room
    print(f"Total price (RM) : {total:.2f}")
    if per_night < 3:
        print("Minimum just 3 nights only for Suite Room.")
else:
    print("Invalid room option! Please re-enter number (1-3): ")
print ("\n")
#Discount will be displayed if user reserves more than 5 rooms of any type
if num_room > 5:
    total_discount = total * 0.1
    print(f"Discount:", total_discount)
#Display user reservation info
print(f"Room Type: ",type_room)
print(f"Per Night: {per_night}")
print(f"Number of Room: {num_room}")

