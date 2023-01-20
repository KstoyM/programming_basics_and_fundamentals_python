from collections import deque

bees = deque(int(x) for x in input().split())
nectars = [int(x) for x in input().split()]
symbols = deque(x for x in input().split())

honey = 0

functions = {
    "*": lambda bee, nec: bee * nec,
    "/": lambda bee, nec: bee / nec,
    "+": lambda bee, nec: bee + nec,
    "-": lambda bee, nec: bee - nec,
}

while nectars and bees:

    curr_bee = bees.popleft()
    curr_nectar = nectars.pop()

    if curr_nectar < curr_bee:
        bees.appendleft(curr_bee)
    elif curr_nectar > curr_bee:
        curr_sym = symbols.popleft()
        honey += abs(functions[curr_sym](curr_bee, curr_nectar))

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join([str(bee) for bee in bees])}")
if nectars:
    print(f"Nectar left: {', '.join([str(nect) for nect in nectars])}")

