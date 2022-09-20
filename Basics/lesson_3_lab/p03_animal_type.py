animal_type = input()

if animal_type == 'dog':
    print('mammal')
elif animal_type in ['crocodile', 'tortoise', 'snake']:
    print('reptile')
else:
    print('unknown')