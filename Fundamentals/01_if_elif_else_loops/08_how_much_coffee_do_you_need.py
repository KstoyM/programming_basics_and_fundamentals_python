command = input()
number_of_coffees = 0

while command != 'END':
    curr_action = command
    if curr_action.islower() and curr_action in ['coding', 'dog', 'cat', 'movie']:
        number_of_coffees += 1
    elif curr_action.isupper() and curr_action in ['CODING', 'DOG', 'CAT', 'MOVIE']:
        number_of_coffees += 2
    command = input()

if number_of_coffees > 5:
    print('You need extra sleep')
else:
    print(f'{number_of_coffees}')