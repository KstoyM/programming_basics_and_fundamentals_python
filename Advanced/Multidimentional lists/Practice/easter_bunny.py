field_size = int(input())

field = []
max_number_of_eggs_collected = 0
bunny_pos = []
best_path = []
best_direction = None

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(field_size):
    field.append(input().split())

    if "B" in field[row]:
        bunny_pos = [row, field[row].index("B")]

for direction, position in directions.items():
    bunny_new_row, bunny_new_col = [
        bunny_pos[0] + position[0],
        bunny_pos[1] + position[1]
    ]
    path = []
    collected_eggs = 0

    while 0 <= bunny_new_row < field_size and 0 <= bunny_new_col < field_size:

        if field[bunny_new_row][bunny_new_col] == 'X':
            break

        collected_eggs += int(field[bunny_new_row][bunny_new_col])
        path.append([bunny_new_row, bunny_new_col])

        bunny_new_row += position[0]
        bunny_new_col += position[1]

        if collected_eggs >= max_number_of_eggs_collected:
            max_number_of_eggs_collected = collected_eggs
            best_path = path
            best_direction = direction


print(best_direction)
print(*best_path, sep="\n")
print(max_number_of_eggs_collected)
