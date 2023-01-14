from collections import deque

numbers = deque()

map_functions = {
    1: lambda x: numbers.append(x[1]),
    2: lambda x: numbers.pop() if numbers else None,
    3: lambda x: print(max(numbers)) if numbers else None,
    4: lambda x: print(min(numbers)) if numbers else None
}

for n in range(int(input())):
    action = [int(i) for i in input().split()]

    map_functions[action[0]](action)

numbers.reverse()

print(*numbers, sep=", ")