def cars_func(cars):
    cars_dict = {}
    for _ in range(cars):
        car_type, mileage, fuel = input().split("|")
        cars_dict[car_type] = [int(mileage), int(fuel)]
    return cars_dict


def drive_func(cars_dict, car, dist, fuel_needed):
    if fuel_needed <= cars_dict[car][1]:
        cars_dict[car][0] += dist
        cars_dict[car][1] -= fuel_needed
        print(f"{car} driven for {dist} kilometers. {fuel_needed} liters of fuel consumed.")
    else:
        print("Not enough fuel to make that ride")
    if cars_dict[car][0] >= 100000:
        del cars_dict[car]
        print(f"Time to sell the {car}!")


def refuel_func(cars_dict, car, fuel_for_refill):
    if cars_dict[car][1] + fuel_for_refill > 75:
        fuel_needed = 75 - cars_dict[car][1]
        cars_dict[car][1] += fuel_needed
        print(f"{car} refueled with {fuel_needed} liters")
    else:
        cars_dict[car][1] += fuel_for_refill
        print(f"{car} refueled with {fuel_for_refill} liters")


def revert_func(cars_dict, car, mileage):
    if cars_dict[car][0] - mileage <= 10000:
        cars_dict[car][0] = 10000
    else:
        cars_dict[car][0] -= mileage
        print(f"{car} mileage decreased by {mileage} kilometers")


def need_for_speed_func(cars):
    data = cars_func(cars)

    while True:
        command = input().split(" : ")

        if command[0] == 'Stop':
            for car in data:
                print(f"{car} -> Mileage: {data[car][0]} kms, Fuel in the tank: {data[car][1]} lt.")
            break

        action = command[0]

        if action == 'Drive':
            car_type, distance, fuel = command[1], int(command[2]), int(command[3])
            drive_func(data, car_type, distance, fuel)

        elif action == 'Refuel':
            car_type, fuel = command[1], int(command[2])
            refuel_func(data, car_type, fuel)

        elif action == 'Revert':
            car_type, kilometers = command[1], int(command[2])
            revert_func(data, car_type, kilometers)


number_of_cars = int(input())
need_for_speed_func(number_of_cars)
