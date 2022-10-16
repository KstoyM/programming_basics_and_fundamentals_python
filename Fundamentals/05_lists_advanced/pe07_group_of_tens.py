input_numbers = [int(number) for number in input().split(", ")]
current_max = 10

while True:
    if not any(input_numbers):
        break

    current_group = [number for number in input_numbers if number <= current_max]
    print(f"Group of {current_max}'s: {current_group}")

    for num in current_group:
        input_numbers.remove(num)

    current_max += 10
