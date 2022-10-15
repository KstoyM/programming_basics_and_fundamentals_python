first_string = input()
second_string = input()

last_printed_word = first_string

for letter in range(len(first_string)):
    left_part = second_string[:letter + 1]
    right_part = first_string[1 + letter:]
    current_string = left_part + right_part
    if current_string != last_printed_word:
        print(f'{current_string}')
        last_printed_word = current_string