from collections import deque


def print_func(total_shakes, total_chocolates, total_cups_of_milk):

    if not total_shakes == 5:
        print("Not enough milkshakes.")
    else:
        print("Great! You made all the chocolate milkshakes needed!")
    if not total_chocolates:
        print("Chocolate: empty")
    else:
        print(f"Chocolate: {', '.join([str(x) for x in total_chocolates])}")
    if not total_cups_of_milk:
        print("Milk: empty")
    else:
        print(f"Milk: {', '.join([str(x) for x in total_cups_of_milk])}")


chocolates = [int(x) for x in input().split(",")]
cups_of_milk = deque(int(x) for x in input().split(","))

milkshakes = 0

while milkshakes != 5 and cups_of_milk and chocolates:

    curr_chocolate = chocolates.pop()
    curr_milk = cups_of_milk.popleft()

    if curr_chocolate <= 0 and curr_milk <= 0:
        continue
    elif curr_chocolate <= 0:
        cups_of_milk.appendleft(curr_milk)
        continue
    elif curr_milk <= 0:
        chocolates.append(curr_chocolate)
        continue

    if curr_chocolate == curr_milk:
        milkshakes += 1

    else:
        cups_of_milk.append(curr_milk)
        chocolates.append(curr_chocolate - 5)

print_func(milkshakes, chocolates, cups_of_milk)
