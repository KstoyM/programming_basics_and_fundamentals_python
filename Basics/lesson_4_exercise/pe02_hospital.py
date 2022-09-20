period = int(input())
treated_patients = 0
untreated_patients = 0
number_of_doctors = 7

for n in range(1, period + 1):
    if untreated_patients > treated_patients and n % 3 == 0:
        number_of_doctors += 1
    number_of_patients = int(input())
    if number_of_patients > number_of_doctors:
        untreated_patients += number_of_patients - number_of_doctors
        for_loop_untreated = number_of_patients - number_of_doctors
        treated_patients += number_of_patients - for_loop_untreated
    else:
        treated_patients += number_of_patients

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')
