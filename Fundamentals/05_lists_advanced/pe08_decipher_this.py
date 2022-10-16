def swap(string):
    return string[-1:] + string[1:-1] + string[:1]


secret_message = input().split()
deciphered_message = []

for word in secret_message:
    if int(word[0]) == 1:
        first_letter = chr(int(word[0] + word[1] + word[2]))
        current_word = word[3:len(word) + 1]
        if len(word) <= 4:
            result_word = first_letter + current_word
        else:
            result_word = first_letter + swap(current_word)
        deciphered_message.append(result_word)
    elif int(word[0]) > 1:
        first_letter = chr(int(word[0] + word[1]))
        current_word = word[2:len(word) + 1]
        if len(word) <= 3:
            result_word = first_letter + current_word
        else:
            result_word = first_letter + swap(current_word)
        deciphered_message.append(result_word)

print(*deciphered_message)
