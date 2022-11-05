words = input().replace(" ", "")
# words = words.replace(" ", "")
words_dict = {}

for char in words:
    if char not in words_dict:
        words_dict[char] = 0
    words_dict[char] += 1

for key in words_dict.keys():
    print(f"{key} -> {words_dict[key]}")