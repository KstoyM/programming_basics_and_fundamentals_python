days_of_plunder = int(input())
daily_plunder = int(input())
target_plunder = float(input())

total_plunder = 0

for day in range(1, days_of_plunder + 1):

    if day % 3 == 0:
        total_plunder += daily_plunder * 1.5

    else:
        total_plunder += daily_plunder

    if day % 5 == 0:
        total_plunder -= total_plunder * 0.3
        continue

if total_plunder >= target_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {total_plunder / target_plunder * 100:.2f}% of the plunder.")