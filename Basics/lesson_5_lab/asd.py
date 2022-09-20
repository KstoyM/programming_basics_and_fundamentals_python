name = input()

current_class = 0
grades_total = 0
classes_failed = 0

while True:
    grade = float(input())
    current_class += 1

    if grade < 4:
        classes_failed += 1

        if classes_failed == 2:
            print(f'{name} has been excluded at {current_class} grade')
            break

        current_class -= 1
    else:
        grades_total += grade

    if current_class == 12:
        average_grade = grades_total / 12
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break