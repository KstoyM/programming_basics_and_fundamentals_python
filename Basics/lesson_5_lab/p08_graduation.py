name = input()

current_class = 0
grades_total = 0
classes_failed = 0

while current_class != 12:
    grade = float(input())
    grades_total += grade

    if grade < 4:
        classes_failed += 1
        current_class -= 1

    if classes_failed == 2:

        print(f'{name} has been excluded at {current_class} grade')
        break

    current_class += 1

if classes_failed < 2:
    print(f'{name} graduated. Average grade: {grades_total / current_class:.2f}')
