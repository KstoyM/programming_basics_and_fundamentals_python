counter = 0
word_progress = ''
count_of_o = 0
count_of_n = 0
count_of_c = 0

command = input()
while command != 'End':
    current_letter = command

    if current_letter == 'o':
        if count_of_o < 1:
            count_of_o += 1
            counter += 1
            command = input()
            continue
    elif current_letter == 'n':
        if count_of_n < 1:
            count_of_n += 1
            counter += 1
            command = input()
            continue
    elif current_letter == 'c':
        if count_of_c < 1:
            count_of_c += 1
            counter += 1
            command = input()
            continue

    if counter == 3:
        counter = 0
        count_of_o = 0
        count_of_n = 0
        count_of_c = 0
        print(f'{word_progress}', end=' ')
        word_progress = ''

    if chr(97) <= current_letter <= chr(122) or chr(65) <= current_letter <= chr(90):
        word_progress += current_letter

    command = input()