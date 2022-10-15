count_of_characters = int(input())

sum_of_characters = 0

for character in range(count_of_characters):
    current_character = input()
    sum_of_characters += ord(current_character)

print(f'The sum equals: {sum_of_characters}')