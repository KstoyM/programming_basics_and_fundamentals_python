import re

input_str = input()

pattern = r"\s([a-z]+(\.|-|_)?([a-z]+)?@[a-z]+\-?([a-z]+)?\.\w+(\.\w+)?)\b"

matches = re.findall(pattern, input_str)

for match in matches:
    print(match[0])