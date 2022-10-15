def is_palindrome(number):
    if number == number[::-1]:
        return True
    return False


received_numbers = input().split(", ")

for num in received_numbers:
    if is_palindrome(num):
        print('True')
    else:
        print('False')