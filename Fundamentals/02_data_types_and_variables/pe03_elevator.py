from math import ceil

persons_to_elevate = int(input())
capacity_of_elevator = int(input())

courses_needed = ceil(persons_to_elevate / capacity_of_elevator)

print(courses_needed)
