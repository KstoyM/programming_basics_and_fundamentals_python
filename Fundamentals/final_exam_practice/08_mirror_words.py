import re

words_string = input()

pattern = r'(@|#){1}([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'

matches = re.findall(pattern, words_string)
mirror_words = []


if matches:
    print(f'{len(matches)} word pairs found!')
    for match in matches:
        word_one = match[1]
        word_two = match[2]
        if word_one == word_two[::-1]:
            mirror_words.append(f'{word_one} <=> {word_two}')
    if len(mirror_words) == 0:
        print('No mirror words!')
    else:
        print(f"The mirror words are: \n{', '.join(mirror_words)}")
else:
    print('No word pairs found!')
    print('No mirror words!')