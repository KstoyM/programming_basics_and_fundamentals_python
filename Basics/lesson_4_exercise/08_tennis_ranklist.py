from math import floor

number_of_tournaments = int(input())
starting_points = int(input())

points_from_tournaments = 0
won_tournaments = 0

for _ in range(number_of_tournaments):
    reached_stage = input()
    if reached_stage == 'W':
        points_from_tournaments += 2000
        won_tournaments += 1
    elif reached_stage == 'F':
        points_from_tournaments += 1200
    elif reached_stage == 'SF':
        points_from_tournaments += 720

print(f'Final points: {starting_points + points_from_tournaments}')
print(f'Average points: {floor(points_from_tournaments / number_of_tournaments)}')
print(f'{won_tournaments / number_of_tournaments:.2%}')