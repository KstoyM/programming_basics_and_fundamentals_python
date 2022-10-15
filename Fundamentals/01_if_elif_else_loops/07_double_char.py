command = input()
repeated_word = ''

while command != 'End':
    curr_string = command
    if curr_string == 'SoftUni':
        command = input()
        continue
    for letter in curr_string:
        repeated_word += letter * 2
    command = input()
    print(repeated_word)
    repeated_word = ''