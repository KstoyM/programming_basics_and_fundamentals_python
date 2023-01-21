# matrix = []
#
# rows = 3
# columns = 2
#
# for row in range(rows):
#     matrix.append([])
#     for column in range(columns):
#         matrix[row].append(0)
#
# print(matrix)

matrix = []

for row in range(3):
    matrix.append([])
    for col in range(3):
        matrix[row].append(col + (row * 3))
print(matrix)

matrix = [[col + (row * 3) for col in range(3)] for row in range(3)]
print(matrix)
