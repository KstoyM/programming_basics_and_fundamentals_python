character_count = int(input())

for character in range(97, 97 + character_count):
    for character2 in range(97, 97 + character_count):
        for character3 in range(97, 97 + character_count):
            print(f'{chr(character)}{chr(character2)}{chr(character3)}')
