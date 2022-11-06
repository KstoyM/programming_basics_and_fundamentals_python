iterations = int(input())

parking = {}


for index in range(iterations):
    command = input().split()

    if command[0] == "register":
        action, username, license_plate_number = command
        if username not in parking:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    else:
        action, username = command
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking[username]

for user, number in parking.items():
    print(f"{user} => {number}")