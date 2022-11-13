input_strings = input().split()
total_sum = 0

for string in input_strings:
    first_letter = string[0]
    last_letter = string[-1]
    number = int(string[1:len(string) - 1])
    if first_letter.isupper():
        total_sum += number / (ord(first_letter) - 64)
    elif first_letter.islower():
        total_sum += number * (ord(first_letter) - 96)
    if last_letter.isupper():
        total_sum -= ord(last_letter) - 64
    elif last_letter.islower():
        total_sum += ord(last_letter) - 96

print(f"{total_sum:.2f}")