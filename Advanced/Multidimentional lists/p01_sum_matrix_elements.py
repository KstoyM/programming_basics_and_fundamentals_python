matrix = []

rows, columns = [int(x) for x in input().split(", ")]

for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

print(*[sum(sum(el) for el in matrix)])
print(matrix)