import re

sentence = input()

pattern = r'((www.)([a-zA-Z0-9-]+)\.[a-z]+([\.a-z]+)?)'

while sentence:

    matches = re.findall(pattern, sentence)

    for match in matches:
        print(match[0])

    sentence = input()
