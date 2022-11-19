import re

input_str = input()
search_word = input()

pattern = fr'\b{search_word}\b'

matches = re.findall(pattern, input_str, flags=re.I)

print(len(matches))
