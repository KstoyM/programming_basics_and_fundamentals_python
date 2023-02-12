matrix = []
rover_pos = []

for row in range(6):
    matrix.append(input().split(" "))
    if "E" in matrix[row]:
        rover_row = row
        rover_col = matrix[row].index("E")

directions = {
    'up': ((-1, 0), (6, 0)),
    'down': ((1, 0), (-6, 0)),
    'left': ((0, -1), (0, 6)),
    'right': ((0, 1), (0, -6))
}

deposits = {
    'W': 'Water',
    'M': 'Metal',
    'C': 'Concrete',
}

deposits_found = set()

command_list = input().split(", ")

for command in command_list:

    rover_row = rover_row + int(directions[command][0][0])
    rover_col = rover_col + int(directions[command][0][1])

    if not 0 <= rover_row < 6:
        rover_row = rover_row + int(directions[command][1][0])
    if not 0 <= rover_col < 6:
        rover_col = rover_col + int(directions[command][1][1])

    if matrix[rover_row][rover_col] in deposits:
        deposits_found.add(matrix[rover_row][rover_col])
        current_deposit = deposits[matrix[rover_row][rover_col]]
        print(f'{current_deposit} deposit found at ({rover_row}, {rover_col})')

    if matrix[rover_row][rover_col] == 'R':
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break

if len(deposits_found) ==  3:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

