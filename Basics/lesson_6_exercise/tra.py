people_in_jury = int(input())

command = input()
grade_current = 0
grade_final = 0
grade_count = 0
grade_count_final = 0
name_of_current_presentation = ''

while command != 'Finish':
    presentation_name = command
    name_of_current_presentation += presentation_name
    grade_current = 0
    grade_count = 0

    for person in range(people_in_jury):
        current_grade = float(input())
        grade_current += current_grade
        grade_count += 1
        grade_final += current_grade
        grade_count_final += 1

    print(f'{name_of_current_presentation} - {grade_current / grade_count:.2f}.')
    name_of_current_presentation = ''
    command = input()

    if command == 'Finish':
        print(f"Student's final assessment is {grade_final / grade_count_final:.2f}.")
        break