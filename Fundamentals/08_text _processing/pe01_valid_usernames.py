usernames = input().split(", ")

for username in usernames:
    is_length_valid = False
    is_username_valid = False
    is_no_redundant_symbols = False
    word_check = ''

    if 3 <= len(username) <= 16:
        is_length_valid = True

    for char in username:
        if char.isalnum() or char == '_' or char == "-":
            word_check += char
            if word_check == username:
                is_username_valid = True

    if " " not in username:
        is_no_redundant_symbols = True
    if is_length_valid and is_username_valid and is_no_redundant_symbols:
        print(username)
