from collections import deque

pizza_orders = deque(map(int, input().split(", ")))
employees = list(map(int, input().split(", ")))

total_pizzas = 0

while True:

    curr_pizza_order = pizza_orders.popleft()
    curr_employee = employees.pop()

    if 0 < curr_pizza_order <= 10:

        if curr_pizza_order <= curr_employee:
            total_pizzas += curr_pizza_order

        else:
            total_pizzas += curr_employee
            curr_pizza_order -= curr_employee
            pizza_orders.appendleft(curr_pizza_order)

    else:
        employees.append(curr_employee)

    if not pizza_orders or not employees:
        break


if not pizza_orders:
    print(f"All orders are successfully completed!\nTotal pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(str(emp) for emp in employees)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(order) for order in pizza_orders)}")
