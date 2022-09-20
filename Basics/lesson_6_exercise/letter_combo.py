first_letter = ord(input())
second_letter = ord(input())
skip_letter = input()
counter = 0

for char in range(first_letter, second_letter + 1):
    for char2 in range(first_letter, second_letter + 1):
        for char3 in range(first_letter, second_letter + 1):
            if chr(char2) != skip_letter and chr(char) != skip_letter and chr(char3) != skip_letter:
                counter += 1
                print(f'{chr(char)}{chr(char2)}{chr(char3)}', end=' ')

print(f'{counter}', end='')