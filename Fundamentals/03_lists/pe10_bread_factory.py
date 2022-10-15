list_of_events = input().split('|')
energy = 100
coins = 100
is_the_bakery_closed = False

for curr_event in list_of_events:
    event_type_and_value = curr_event.split('-')
    event_type = event_type_and_value[0]
    event_value = int(event_type_and_value[1])

    if event_type == 'rest':
        if energy + event_value <= 100:
            energy += event_value
            print(f'You gained {event_value} energy.')
        else:
            gained_energy = 100 - energy
            energy = 100
            print(f'You gained {gained_energy} energy.')
        print(f"Current energy: {energy}.")

    elif event_type == "order":
        if energy >= 30:
            energy -= 30
            coins += event_value
            print(f'You earned {event_value} coins.')
        else:
            energy += 50
            print("You had to rest!")
            continue

    else:
        if coins >= event_value:
            coins -= event_value
            print(f"You bought {event_type}.")
        else:
            print(f'Closed! Cannot afford {event_type}.')
            is_the_bakery_closed = True
            break

if not is_the_bakery_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")