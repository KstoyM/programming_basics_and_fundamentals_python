matrix = [input().split() for _ in range(int(input().split()[0]))]

square_matrices = 0

for row in range(len(matrix) - 1):
    for col in range(len(matrix[0]) - 1):
        curr_el = matrix[row][col]

        if curr_el == matrix[row][col + 1] and curr_el == matrix[row + 1][col] and curr_el == matrix[row + 1][col + 1]:
            square_matrices += 1

print(square_matrices)