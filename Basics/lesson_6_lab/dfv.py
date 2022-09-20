destination = input()
saved_money = 0
while destination != "End":
    budget_needed = float(input())
    while saved_money <= budget_needed:
        money = float(input())
        saved_money += money
        if saved_money >= budget_needed:
            print(f"Going to {destination}!")
            break
    saved_money = 0
    destination = input()