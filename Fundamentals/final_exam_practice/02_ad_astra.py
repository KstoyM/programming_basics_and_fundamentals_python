import re

string_input = input()

pattern = r'(\||#)([A-Za-z ]+)\1(\d\d/\d\d/\d\d)\1(\d{1,5})\1'

matches = re.findall(pattern, string_input)
foodec = 0

for match in matches:
    calories = match[3]
    foodec += int(calories)

days_we_can_last = foodec // 2000
print(f'You have food to last you for: {days_we_can_last} days!')

for match in matches:
    item_name = match[1]
    exp_date = match[2]
    calories = match[3]
    if matches:
        print(f"Item: {item_name}, Best before: {exp_date}, Nutrition: {calories}")