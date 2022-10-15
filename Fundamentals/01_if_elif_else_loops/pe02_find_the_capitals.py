string = input()

capital_positions = list(string)
counter = -1

for letter in string:
    counter += 1
    if 65 <= ord(letter) <= 90:
        capital_positions += str(counter)
print('[', end='')
print(', '.join(capital_positions), end='')
print(']', end='')