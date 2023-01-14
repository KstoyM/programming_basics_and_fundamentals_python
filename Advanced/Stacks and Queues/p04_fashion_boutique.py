clothes_box = [int(x) for x in input().split()]
rack_initial_capacity = int(input())
rack_capacity = rack_initial_capacity
rack_counter = 1

for cloth in clothes_box[::-1]:

    if rack_capacity - cloth < 0:
        rack_counter += 1
        rack_capacity = rack_initial_capacity - cloth
    else:
        rack_capacity -= cloth

print(rack_counter)