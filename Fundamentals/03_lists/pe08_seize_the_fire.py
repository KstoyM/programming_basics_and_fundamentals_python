cell_type = input().split('#')
cell_type_2 = []

for element in cell_type:
    element2 = element.replace('=', ' ')
    cell_type_2.append(element2)

water_quantity = int(input())
total_effort = 0
total_fire = 0

print('Cells:')
for room in cell_type_2:
    is_room_valid = False
    room_value = int(room[-3::])
    if 'High' in room and 81 <= room_value <= 125:
        is_room_valid = True
    elif 'Medium' in room and 51 <= room_value <= 80:
        is_room_valid = True
    elif 'Low' in room and 1 <= room_value <= 50:
        is_room_valid = True

    if is_room_valid and water_quantity >= room_value:
        water_quantity -= room_value
        total_effort += 0.25 * room_value
        total_fire += room_value
        print(f' - {room_value}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')