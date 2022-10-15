people = int(input())
lift = [int(cabins) for cabins in input().split()]
capacity = len(lift) * 4 - sum(lift)

for cabin in range(len(lift)):
    people_to_load = min(people, (4 - lift[cabin]))
    capacity -= people_to_load
    people -= people_to_load
    lift[cabin] += people_to_load

if people == 0 and capacity > 0:
    print(f"The lift has empty spots!")

elif people > 0 and capacity == 0:
    print(f"There isn't enough space! {people} people in a queue!")

print(*lift)