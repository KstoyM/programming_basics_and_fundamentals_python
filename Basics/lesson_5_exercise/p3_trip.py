money_needed_for_trip = float(input())
money_available = float(input())

days_counter = 0
days_spending_in_a_row = 0

while True:
    activity = input()
    money_spent_or_saved = float(input())
    days_counter += 1

    if activity == 'save':
        money_available += money_spent_or_saved

    if activity == 'spend':
        if money_available < money_spent_or_saved:
            money_available = 0
        else:
            money_available -= money_spent_or_saved

    if money_needed_for_trip <= money_available:
        print(f'You saved the money for {days_counter} days.')
        break

    if activity == 'spend':
        days_spending_in_a_row += 1
    else:
        days_spending_in_a_row = 0

    if days_spending_in_a_row >= 5:
        print(f"You can't save the money.")
        print(f"{days_counter}")
        break
