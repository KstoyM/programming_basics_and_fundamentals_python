sequence_input = input().split()
abs_values = []

for value in sequence_input:
    abs_values.append(abs(float(value)))

print(abs_values)
