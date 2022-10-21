employees = 3
employee_efficiency = 0

for employees in range(employees):
    employee_efficiency += int(input())

students_count = int(input())

time_for_reset = 0
time_passed = 0

while True:
    if students_count < employee_efficiency:
        if students_count <= 0:
            break
        else:
            time_passed += 1
            break

    else:
        if time_for_reset % 3 == 0 and time_for_reset != 0:
            time_passed += time_for_reset + 1
            time_for_reset = 0
            continue
        else:
            students_count -= employee_efficiency
            time_for_reset += 1

print(f'Time needed: {time_passed + time_for_reset}h.')