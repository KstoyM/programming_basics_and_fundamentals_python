sequence_one = set(int(n) for n in input().split())
sequence_two = set(int(i) for i in input().split())

functions = {
    "Add First": lambda x: [sequence_one.add(el) for el in x],
    "Add Second": lambda x: [sequence_two.add(el) for el in x],
    "Remove First": lambda x: [sequence_one.discard(el) for el in x],
    "Remove Second": lambda x: [sequence_two.discard(el) for el in x],
    "Check Subset": lambda: print(True) if sequence_one.issubset(sequence_two) or sequence_two.issubset(sequence_one)
    else print(False)
}

for _ in range(int(input())):
    first_command, *data = input().split()

    command = first_command + " " + data.pop(0)

    if data:
        functions[command]([int(x) for x in data])
    else:
        functions[command]()

print(*sorted(sequence_one), sep=", ")
print(*sorted(sequence_two), sep=", ")
