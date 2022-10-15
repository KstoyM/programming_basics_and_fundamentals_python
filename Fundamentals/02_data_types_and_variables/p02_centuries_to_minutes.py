centuries = int(input())

years_in_a_century = centuries * 100
days_in_a_century = int(years_in_a_century * 365.2422)
hours_in_a_century = days_in_a_century * 24
minutes_in_a_century = hours_in_a_century * 60

print(f'{centuries} centuries = {years_in_a_century} years = {days_in_a_century} days = {hours_in_a_century} '
      f'hours = {minutes_in_a_century} minutes')