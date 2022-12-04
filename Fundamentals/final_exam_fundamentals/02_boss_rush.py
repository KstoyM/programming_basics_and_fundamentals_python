import re

iterations = int(input())
pattern = r'(\|)([A-Z]{4,})\1:(#)([A-Za-z]+ [A-Za-z]+)\3'

for _ in range(iterations):
    boss_name = input()
    match = re.findall(pattern, boss_name)
    if match:
        boss = match[0][1]
        title = match[0][3]
        print(f"{boss}, The {title}")
        print(f">> Strength: {len(boss)}")
        print(f">> Armor: {len(title)}")
    else:
        print("Access denied!")