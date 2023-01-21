rows = int(input())

matrix = [input().split(", ") for _ in range(rows)]

result = []

for row in matrix:
    for num in row:
        result.append(int(num))

print(result)