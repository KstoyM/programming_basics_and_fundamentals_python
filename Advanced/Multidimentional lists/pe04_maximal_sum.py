rows, cols = [int(x) for x in input().split()]

matrix = [[int(el) for el in input().split()] for _ in range(rows)]
current_max = float('-inf')
current_max_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        current_matrix = [[matrix[row][col], matrix[row][col + 1], matrix[row][col+2]],
                          [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col+2]],
                          [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]]

        current_matrix_sum = sum([sum(el) for el in current_matrix])

        if current_matrix_sum > current_max:
            current_max = current_matrix_sum
            current_max_matrix = current_matrix
            current_matrix_sum = 0

print(f'Sum = {current_max}')
[print(*current_max_matrix[row]) for row in range(3)]