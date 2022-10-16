input_names = input().split(", ")
sorted_names = sorted(input_names, key=lambda x: (-len(x), x))

print(sorted_names)