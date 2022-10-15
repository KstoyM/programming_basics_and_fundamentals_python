numbers = input().split()
rounded_numbers = []

for element in numbers:
    rounded_numbers.append(round(float(element)))

print(rounded_numbers)