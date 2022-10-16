wagons = int(input())
train = [0] * wagons

command = input()

while True:

    if command == 'End':
        break

    current_command = command.split()

    if 'add' in current_command:
        people_in_wagon = train.pop(-1)
        people_to_insert = people_in_wagon + int(current_command[1])
        train.append(people_to_insert)

    elif 'insert' in current_command:
        people_in_wagon = train.pop(int(current_command[1]))
        people_to_insert = people_in_wagon + int(current_command[2])
        train.insert(int(current_command[1]), people_to_insert)

    elif 'leave' in current_command:
        people_in_wagon = train.pop(int(current_command[1]))
        people_to_insert = people_in_wagon - int(current_command[2])
        train.insert(int(current_command[1]), people_to_insert)

    command = input()

print(train)
