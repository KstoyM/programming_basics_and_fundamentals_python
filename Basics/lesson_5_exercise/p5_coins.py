from math import floor

total_amt = float(input())

coins_amt = total_amt * 100
coins_amt = floor(coins_amt)
coins = 0

while coins_amt > 0:
    if coins_amt >= 200:
        coins_amt -= 200
        coins += 1

    elif coins_amt >= 100:
        coins_amt -= 100
        coins += 1

    elif coins_amt >= 50:
        coins_amt -= 50
        coins += 1

    elif coins_amt >= 20:
        coins_amt -= 20
        coins += 1

    elif coins_amt >= 10:
        coins_amt -= 10
        coins += 1

    elif coins_amt >= 5:
        coins_amt -= 5
        coins += 1

    elif coins_amt >= 2:
        coins_amt -= 2
        coins += 1

    elif coins_amt >= 1:
        coins_amt -= 1
        coins += 1

    elif coins_amt == 0:
        break

print(int(coins))