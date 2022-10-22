from math import ceil

number_of_the_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

attendances_of_max_student = 0
current_max = 0
# {total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})

for student in range(number_of_the_students):

    student_attendance = int(input())

    current_total_bonus = student_attendance / number_of_lectures * (5 + additional_bonus)

    if current_max < current_total_bonus:
        current_max = current_total_bonus
        attendances_of_max_student = student_attendance

print(f"Max Bonus: {ceil(current_max)}.")
print(f"The student has attended {attendances_of_max_student} lectures.")