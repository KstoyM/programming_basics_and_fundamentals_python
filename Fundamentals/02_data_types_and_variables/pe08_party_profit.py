group_size = int(input())
days_of_adventure = int(input())

gold_coins = 0

for day in range(1, days_of_adventure + 1):

    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    gold_coins += 50
    gold_coins -= group_size * 2

    if day % 3 == 0:
        gold_coins -= group_size * 3

    if day % 5 == 0:
        gold_coins += 20 * group_size
        if day % 3 == 0:
            gold_coins -= group_size * 2

print(f'{group_size} companions received {int(gold_coins / group_size)} coins each.')