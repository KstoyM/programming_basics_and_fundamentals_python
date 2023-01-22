matrix = [[int(r) for r in input().split(", ")] for _ in range(int(input().split(", ")[0]))]
current_max = float('-inf')
current_sum = 0
max_matrix = []

for row in range(len(matrix) - 1):
    for col in range(len(matrix[0]) - 1):
        current_sum += matrix[row][col] + matrix[row + 1][col] \
                       + matrix[row][col + 1] + matrix[row + 1][col + 1]

        if current_sum > current_max:
            current_max = current_sum
            max_matrix = [[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]

        current_sum = 0

[print(*el) for el in max_matrix]
print(current_max)