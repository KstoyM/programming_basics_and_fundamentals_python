width_space = int(input())
length_space = int(input())
height_space = int(input())

total_space = width_space * length_space * height_space

curr_command = input()

while curr_command != 'Done':
    number_of_boxes = int(curr_command)
    total_space -= number_of_boxes

    if total_space <= 0:
        break
    else:
        curr_command = input()

if curr_command == 'Done':
    print(f'{total_space} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(total_space)} Cubic meters more.')