from collections import deque

pumps = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

pumps_copy = pumps.copy()
fuel = 0
current_index = 0

while pumps_copy:

    petrol_amt, distance_from_pump = pumps_copy.popleft()
    fuel += petrol_amt

    if fuel - distance_from_pump < 0:
        pumps.rotate(-1)
        pumps_copy = pumps.copy()
        current_index += 1
        fuel = 0
    else:
        fuel -= distance_from_pump

print(current_index)
