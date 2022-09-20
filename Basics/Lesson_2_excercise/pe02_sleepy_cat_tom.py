vacation_leave_days = int(input())

days_in_a_year = 365
maximum_play_minutes = 30000
number_of_minutes_played_while_on_vacation = vacation_leave_days * 127
number_of_minutes_played_while_not_on_vacation = (days_in_a_year - vacation_leave_days) * 63
total_minutes_played = number_of_minutes_played_while_on_vacation + number_of_minutes_played_while_not_on_vacation
# total_minutes_played_in_hours = total_minutes_played // 60
# remaining_minutes = total_minutes_played % 60

if total_minutes_played > maximum_play_minutes:
    print(f'Tom will run away')
    print(f'{(total_minutes_played - maximum_play_minutes) // 60} hours '
          f'and {(total_minutes_played - maximum_play_minutes) % 60} minutes more for play')
else:
    print(f'Tom sleeps well')
    print(f'{(maximum_play_minutes - total_minutes_played) // 60} hours '
          f'and {(maximum_play_minutes - total_minutes_played) % 60} minutes less for play')