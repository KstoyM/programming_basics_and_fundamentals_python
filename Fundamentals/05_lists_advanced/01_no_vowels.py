vowels = ['a', 'o', 'u', 'e', 'i']

text = input()
no_vowels_text = [letter for letter in text if letter.lower() not in vowels]
print("".join(no_vowels_text))