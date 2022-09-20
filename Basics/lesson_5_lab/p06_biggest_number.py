import sys

command = input()
highest_number = -sys.maxsize

while command != 'Stop':
    number = int(command)
    if number > highest_number:
        highest_number = number

    command = input()

print(highest_number)