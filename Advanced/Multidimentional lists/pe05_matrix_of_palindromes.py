rows, cols = [int(el) for el in input().split()]

matrix = []
matrix_row = []

for row in range(rows):
    matrix_row = []
    for col in range(cols):
        first_letter = chr(row + 97)
        middle_letter = chr(row + 97 + col)
        last_letter = chr(row + 97)
        palindrome = first_letter + middle_letter + last_letter
        matrix_row.append(palindrome)
    matrix.append(matrix_row)
[print(*el) for el in matrix]
