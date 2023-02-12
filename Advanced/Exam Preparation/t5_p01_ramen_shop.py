from collections import deque

bowls_of_ramen = list(map(int, input().split(", ")))
customers = deque(map(int, input().split(", ")))

while bowls_of_ramen and customers:

    current_ramen_bowl = bowls_of_ramen.pop()
    current_customer = customers.popleft()
    is_cycle_completed = False

    if current_ramen_bowl == current_customer:
        continue

    while current_ramen_bowl > current_customer:

        current_ramen_bowl -= current_customer
        if customers:
            current_customer = customers.popleft()
        else:
            bowls_of_ramen.append(current_ramen_bowl)
            is_cycle_completed = True
            break
        if current_customer > current_ramen_bowl:
            bowls_of_ramen.append(current_ramen_bowl)
            customers.appendleft(current_customer)
            is_cycle_completed = True
            break

    if is_cycle_completed:
        continue

    while current_customer > current_ramen_bowl:

        current_customer -= current_ramen_bowl
        if bowls_of_ramen:
            current_ramen_bowl = bowls_of_ramen.pop()
        else:
            customers.appendleft(current_customer)
            break

        if current_ramen_bowl > current_customer:
            bowls_of_ramen.append(current_ramen_bowl)
            customers.appendleft(current_customer)
            break

if bowls_of_ramen:
    print("Great job! You served all the customers.")
    print(f"Bowls of ramen left: {', '.join(str(b) for b in bowls_of_ramen)}")
elif customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(c) for c in customers)}")
else:
    print("Great job! You served all the customers.")