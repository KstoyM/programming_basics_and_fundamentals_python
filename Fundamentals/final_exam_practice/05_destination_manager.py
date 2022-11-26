# My solution

import re

input_str = input()

pattern = r'(=|\/)[A-Z][A-Za-z]{2,}\1'

matches = re.finditer(pattern, input_str)
destinations = []
match_points = 0

for match in matches:
    destination = match.group()
    destination = destination.strip("/=")
    match_points += len(destination)
    destinations.append(destination)

print(f'Destinations: {", ".join(destinations)}')
print(f'Travel Points: {match_points}')

# Mario's solution

# import re
#
# data = input()
# pattern = r'(=|\/)[A-Z][A-Za-z]{2,}\1'
# result = re.finditer(pattern, data)
#
# points = 0
# all_destinations = []
#
# for destination in result:
#     current_destination = re.split('/|=', destination.group())[1]
#     points += len(current_destination)
#     all_destinations.append(current_destination)
#
# print(f"Destinations: {', '.join(all_destinations)}")
# print(f"Travel Points: {points}")