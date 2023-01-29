matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
index_validation = list(range(len(matrix)))

while True:

    command = input().split()

    if command[0] == 'END':
        break

    action, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3])

    if action == 'Add':
        if row in index_validation and col in index_validation:
            matrix[row][col] += value
        else:
            print("Invalid coordinates")

    elif action == "Subtract":
        if row in index_validation and col in index_validation:
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")

[print(*x) for x in matrix]