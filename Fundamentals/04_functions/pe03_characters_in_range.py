def char_in_range(first_char, second_char):
    final_list = []
    for ch in range(ord(first_char) + 1, ord(second_char)):
        final_list.append(chr(ch))
    return final_list


char1 = input()
char2 = input()

print(" ".join(char_in_range(char1, char2)))
