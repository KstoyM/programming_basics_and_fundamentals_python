from collections import deque

quant_food = int(input())
orders_que = deque([int(x) for x in input().split()])

print(max(orders_que))

if quant_food - sum(orders_que) >= 0:
    print('Orders complete')
else:
    while True:
        current_order = orders_que.popleft()
        quant_food -= current_order
        if quant_food < 0:
            orders_que.appendleft(current_order)
            print(f"Orders left: {' '.join([str(o) for o in orders_que])}")
            break