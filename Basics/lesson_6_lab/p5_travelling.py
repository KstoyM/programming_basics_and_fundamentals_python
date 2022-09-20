destination = input()
budget_needed = float(input())

total_saved = 0

command = input()

while command != 'End':
    saved_money = float(command)
    total_saved += saved_money

    if total_saved >= budget_needed:
        print(f'Going to {destination}!')
        total_saved = 0
        destination = input()
        while type(destination) == float:
            destination = input()
        else:
            budget_needed = float(input())
            command = input()
    else:
        command = input()