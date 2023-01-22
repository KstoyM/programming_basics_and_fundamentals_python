matrix = [[int(r) for r in input().split(", ")] for _ in range(int(input()))]

primary_diag = []
secondary_diag = []

for row in range(len(matrix)):
    primary_diag.append(matrix[row][row])
    secondary_diag.append(matrix[::-1][row][row])

print(f"Primary diagonal: {', '.join([str(el) for el in primary_diag])}. Sum: {sum(primary_diag)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in secondary_diag[::-1]])}. Sum: {sum(secondary_diag)}")