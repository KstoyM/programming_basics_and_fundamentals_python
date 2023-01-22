from collections import deque

rows, cols = [int(x) for x in input().split()]

matrix = []

keyword = list(input())
keyword_copy = deque(keyword)

for row in range(rows):
    while len(keyword_copy) < cols:
        keyword_copy.extend(keyword)

    if row % 2 == 0:
        print(*[keyword_copy.popleft() for _ in range(cols)], sep="")
    else:
        print(*[keyword_copy.popleft() for _ in range(cols)][::-1], sep="")
