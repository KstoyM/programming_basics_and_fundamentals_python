import re

sentence = input()

pattern = r'\b_([a-zA-Z0-0]+\b)'

matches = re.findall(pattern, sentence)
print(','.join(matches))