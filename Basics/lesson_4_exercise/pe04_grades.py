number_of_students = int(input())

number_of_top_students = 0
number_of_good_students = 0
number_of_bad_students = 0
number_of_failed_students = 0
number_of_total_students = 0
amount_of_grades = 0

for student in range(number_of_students):
    grade_of_student = float(input())
    number_of_total_students += 1
    amount_of_grades += grade_of_student
    if grade_of_student >= 5:
        number_of_top_students += 1
    elif grade_of_student >= 4:
        number_of_good_students += 1
    elif grade_of_student >= 3:
        number_of_bad_students += 1
    else:
        number_of_failed_students += 1

print(f'Top students: {number_of_top_students / number_of_total_students:.2%}')
print(f'Between 4.00 and 4.99: {number_of_good_students / number_of_total_students:.2%}')
print(f'Between 3.00 and 3.99: {number_of_bad_students / number_of_total_students:.2%}')
print(f'Fail: {number_of_failed_students / number_of_total_students:.2%}')
print(f'Average: {amount_of_grades / number_of_total_students:.2f}')