rows, cols = [int(x) for x in input().split(" ")]

matrix = []
moves_made = 0
touched_opponents = 0

DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(rows):
    matrix.append(input().split(" "))

    if "B" in matrix[row]:
        player_pos = [int(row), int(matrix[row].index("B"))]

while touched_opponents < 3:

    command = input()

    if command == 'Finish':
        break

    player_pos = [player_pos[0] + DIRECTIONS[command][0], player_pos[1] + DIRECTIONS[command][1]]

    if not 0 <= player_pos[0] < rows or not 0 <= player_pos[1] < cols:
        player_pos = [player_pos[0] - DIRECTIONS[command][0], player_pos[1] - DIRECTIONS[command][1]]
        continue

    whats_on_board = matrix[player_pos[0]][player_pos[1]]

    if whats_on_board == 'P':
        touched_opponents += 1
        matrix[player_pos[0]][player_pos[1]] = '-'

    elif whats_on_board == 'O':
        player_pos = [player_pos[0] - DIRECTIONS[command][0], player_pos[1] - DIRECTIONS[command][1]]
        continue

    moves_made += 1

print('Game over!')
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")