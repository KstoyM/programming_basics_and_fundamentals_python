size = int(input())
car_number = input()
track = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

car_position = [0, 0]
distance_covered = 0
tunnel_positions = []

for line in range(size):
    track.append(input().split())
    if 'T' in track[line]:
        tunnel_index = track[line].index('T')
        tunnel_positions.append([int(line), int(tunnel_index)])

is_the_race_finished = False
command = input()

while command != 'End':

    car_row = car_position[0] + directions[command][0]
    car_col = car_position[1] + directions[command][1]
    car_position = [car_row, car_col]

    if car_position in tunnel_positions:
        for position in tunnel_positions:
            track[position[0]][position[1]] = '.'

        tunnel_positions.remove([car_row, car_col])
        new_row = tunnel_positions[0][0]
        new_col = tunnel_positions[0][1]
        car_position = [int(new_row), int(new_col)]
        distance_covered += 30
    else:
        distance_covered += 10

    current_track_position = track[car_position[0]][car_position[1]]

    if current_track_position == 'F':
        is_the_race_finished = True
        break

    command = input()

if is_the_race_finished:
    print(f'Racing car {car_number} finished the stage!')
else:
    print(f"Racing car {car_number} DNF.")

print(f"Distance covered {distance_covered} km.")

track[car_position[0]][car_position[1]] = 'C'
[print(''.join(row)) for row in track]