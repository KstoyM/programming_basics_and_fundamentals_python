import random

number = random.randint(1, 3)

guess_number = int(input('Въведи число от 1 до 3: '))

if number == guess_number:
    print('Ти спечели играта')
else:
    print('Ти загуби играта')