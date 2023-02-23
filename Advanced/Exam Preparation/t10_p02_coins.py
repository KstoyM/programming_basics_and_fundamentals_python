SIZE = int(input())

matrix = []
player_positions = []
collected_coins = 0

for row in range(SIZE):
    matrix.append(input().split(" "))
    if "P" in matrix[row]:
        player_pos = [int(row), int(matrix[row].index("P"))]
        matrix[row][player_pos[1]] = 0

player_positions.append(player_pos)

directions = {
    'up': ((-1, 0), (SIZE, 0)),
    'down': ((1, 0), (-SIZE, 0)),
    'left': ((0, -1), (0, SIZE)),
    'right': ((0, 1), (0, -SIZE))
}

while collected_coins < 100:

    curr_direction = input()
    if curr_direction in directions:
        player_pos = [player_pos[0] + directions[curr_direction][0][0], player_pos[1] + directions[curr_direction][0][1]]
    else:
        continue

    if not 0 <= player_pos[0] < SIZE or not 0 <= player_pos[1] < SIZE:
        player_pos = [player_pos[0] + directions[curr_direction][1][0],
                      player_pos[1] + directions[curr_direction][1][1]]

    current_item = matrix[player_pos[0]][player_pos[1]]

    if current_item == 'X':
        collected_coins = int(collected_coins // 2)
        player_positions.append(player_pos)
        break

    else:
        collected_coins += int(current_item)
        matrix[player_pos[0]][player_pos[1]] = 0
        player_positions.append(player_pos)

if collected_coins >= 100:
    print(f"You won! You've collected {collected_coins} coins.")
else:
    print(f"Game over! You've collected {collected_coins} coins.")
print(f"Your path:")
[print(pos) for pos in player_positions]

