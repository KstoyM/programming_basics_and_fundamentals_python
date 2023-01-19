parking = set()

COMMAND_IN = 'IN'
COMMAND_OUT = 'OUT'

for _ in range(int(input())):
    action, plate_number = input().split(", ")

    if action == COMMAND_IN:
        parking.add(plate_number)
    else:
        parking.remove(plate_number)

if parking:
    for car in parking:

        print(car)
else:
    print("Parking Lot is Empty")