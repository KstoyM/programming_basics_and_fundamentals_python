matrix = [[int(el) for el in input().split()] for _ in range(int(input()))]

prim_diag = 0
sec_diag = 0

for row in range(len(matrix)):
    prim_diag += matrix[row][row]
    sec_diag += matrix[len(matrix) - row - 1][row]

print(abs(prim_diag - sec_diag))