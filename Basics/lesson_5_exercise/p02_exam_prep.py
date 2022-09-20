max_failed_grades = int(input())

name_of_exercise = input()
cnt_failed_exercises = 0
cnt_of_done_exercises = 0
total_score = 0
last_problem = ''

while name_of_exercise != 'Enough':
    score_from_exercise = int(input())
    total_score += score_from_exercise
    cnt_of_done_exercises += 1
    last_problem = name_of_exercise

    if score_from_exercise <= 4:
        cnt_failed_exercises += 1

    if cnt_failed_exercises == max_failed_grades:
        print(f'You need a break, {cnt_failed_exercises} poor grades.')
        break
    name_of_exercise = input()

if cnt_failed_exercises < max_failed_grades:
    average_score = total_score / cnt_of_done_exercises
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {cnt_of_done_exercises}')
    print(f'Last problem: {last_problem}')