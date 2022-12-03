import re

emoji = input()
cool_threshold = 1

pattern = r'(:|\*){2}[A-Z][a-z]{2,}\1{2}'
cool_emoji_list = []
emoji_count = 0

digit_matches = re.findall("\d", emoji)

for element in digit_matches:
    cool_threshold *= int(element)
print(f'Cool threshold: {cool_threshold}')

emoji_matches = re.finditer(pattern, emoji)

for element in emoji_matches:
    cool_number = 0
    emoji_count += 1
    for char in element.group():
        if char not in [":", "*"]:
            cool_number += ord(char)
    if cool_number >= cool_threshold:
        cool_emoji_list.append(element.group())

print(f'{emoji_count} emojis found in the text. The cool ones are:')
for element in cool_emoji_list:
    print(element)
