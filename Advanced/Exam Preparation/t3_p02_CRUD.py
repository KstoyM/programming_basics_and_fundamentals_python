def create_func(matrix, value):
    if matrix[position[0]][position[1]] == '.':
        matrix[position[0]][position[1]] = value


def update_func(matrix, value):
    if matrix[position[0]][position[1]].isalnum():
        matrix[position[0]][position[1]] = value


def delete_func(matrix):
    if matrix[position[0]][position[1]].isalnum():
        matrix[position[0]][position[1]] = '.'


def read_func(matrix):
    if matrix[position[0]][position[1]].isalnum():
        print(matrix[position[0]][position[1]])


size = 6
matrix = []

DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    matrix.append(input().split())

position = [x for x in input() if x.isdigit()]

while True:

    command = input().split(', ')
    action = command[0]

    if action == 'Stop':
        break

    direction = command[1]

    position = (DIRECTIONS[direction][0] + int(position[0]), DIRECTIONS[direction][1] + int(position[1]))

    if action == 'Create':
        value = command[2]
        create_func(matrix, value)
    elif action == 'Update':
        value = command[2]
        update_func(matrix, value)
    elif action == 'Delete':
        delete_func(matrix)
    elif action == 'Read':
        read_func(matrix)

[print(*row) for row in matrix]
