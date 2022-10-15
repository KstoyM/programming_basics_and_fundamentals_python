def check_length(password):
    if len(password) < 6 or len(password) > 10:
        print('Password must be between 6 and 10 characters')
    else:
        return True


def check_characters(password):
    if not password.isalnum():
        print("Password must consist only of letters and digits")
    else:
        return True


def check_digits(password):
    digits_counter = 0
    for char in password:
        if char.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        print("Password must have at least 2 digits")
    else:
        return True


input_password = input()
validator = check_length(input_password), check_characters(input_password), check_digits(input_password)
if all(validator):
    print('Password is valid')
