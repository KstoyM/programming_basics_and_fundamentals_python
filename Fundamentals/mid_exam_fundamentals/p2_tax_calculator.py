vehicle_string = input().split(">>")
total_tax_collected = 0

for vehicle in vehicle_string:
    vehicle_type, years_in_duty, km_travelled = vehicle.split()
    years_in_duty = int(years_in_duty)
    km_travelled = int(km_travelled)
    tax_of_current_car = 0
    if vehicle_type == "family":
        tax_of_current_car += 50 - (years_in_duty * 5)
        tax_of_current_car += km_travelled // 3000 * 12
    elif vehicle_type == "heavyDuty":
        tax_of_current_car += 80 - (years_in_duty * 8)
        tax_of_current_car += km_travelled // 9000 * 14
    elif vehicle_type == "sports":
        tax_of_current_car += 100 - (years_in_duty * 9)
        tax_of_current_car += km_travelled // 2000 * 18
    else:
        print("Invalid car type.")
        continue
    total_tax_collected += tax_of_current_car
    print(f"A {vehicle_type} car will pay {tax_of_current_car:.2f} euros in taxes.")

print(f"The National Revenue Agency will collect {total_tax_collected:.2f} euros in taxes.")