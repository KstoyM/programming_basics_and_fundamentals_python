palindrome_strings = [string for string in input().split() if string == string[::-1]]
palindrome_for_counting = input()

palindrome_count_in_list = palindrome_strings.count(palindrome_for_counting)

print(palindrome_strings)
print(f'Found palindrome {palindrome_count_in_list} times')
