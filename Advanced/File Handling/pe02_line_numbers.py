from string import punctuation
import re

pattern = r"(-[A-Za-z0-9\s,'.?!:]+[\.|\!|\?])"

with open('text.txt', 'r') as file:
    text = file.readlines()
    text_as_str = ", ".join(text)
    matches = re.findall(pattern, text_as_str)

with open('output.txt', 'w') as output:

    for line in range(len(matches)):
        letters = 0
        symbols = 0
        for letter in matches[line]:
            if letter.isalpha():
                letters += 1
            elif letter in punctuation:
                symbols += 1

        output.write(f'Line {line}: {matches[line]} ({letters})({symbols})\n')