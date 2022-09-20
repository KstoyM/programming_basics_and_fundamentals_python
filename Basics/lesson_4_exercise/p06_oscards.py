nominee = input()
points_from_academy = float(input())
number_of_jury = int(input())
total_points = 0


for n in range(number_of_jury):
    jury_member = input()
    points_of_jury_member = float(input())
    total_points += (len(jury_member) * points_of_jury_member) / 2
    if total_points + points_from_academy > 1250.5:
        print(f'Congratulations, {nominee} got a nominee for leading role '
              f'with {total_points + points_from_academy:.1f}!')
        break

if points_from_academy + total_points < 1250.5:
    print(f'Sorry, {nominee} you need {1250.5 - total_points - points_from_academy:.1f} more!')