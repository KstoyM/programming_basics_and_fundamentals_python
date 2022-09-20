import sys

command = input()
lowest_number = sys.maxsize

while command != 'Stop':
    number = int(command)
    if number < lowest_number:
        lowest_number = number

    command = input()

print(lowest_number)