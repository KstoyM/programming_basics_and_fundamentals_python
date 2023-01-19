reservations = set()
attendance_set = set()

for index in range(int(input())):
    reservation = input()
    reservations.add(reservation)

while True:

    command = input()

    if command == "END":
        break

    else:
        attendance_set.add(command)

difference = reservations.difference(attendance_set)

print(len(difference))
for el in sorted(difference):
    print(el)