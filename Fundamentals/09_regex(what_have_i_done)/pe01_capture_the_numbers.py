import re

pattern = r"\d+"
numbers = input()

while numbers:

    matches = re.findall(pattern, numbers)
    if matches:
        print(' '.join(matches), end=' ')
    numbers = input()

# https://judge.softuni.org/Contests/Compete/Index/1743#0