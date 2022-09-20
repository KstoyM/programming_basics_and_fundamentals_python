cnt_of_loads = int(input())

price_per_ton = 0
total_price = 0
total_weight = 0
p_bus_load = 0
p_truck_load = 0
p_train_load = 0

for n in range(cnt_of_loads):
    weight_of_load = int(input())
    total_weight += weight_of_load
    if weight_of_load <= 3:
        p_bus_load += weight_of_load
        price_per_ton = 200
    elif weight_of_load <= 11:
        p_truck_load += weight_of_load
        price_per_ton = 175
    else:
        p_train_load += weight_of_load
        price_per_ton = 120
    total_price += price_per_ton * weight_of_load

average_price_per_ton = total_price / total_weight

print(f'{average_price_per_ton:.2f}')
print(f'{p_bus_load / total_weight:.2%}')
print(f'{p_truck_load / total_weight:.2%}')
print(f'{p_train_load / total_weight:.2%}')