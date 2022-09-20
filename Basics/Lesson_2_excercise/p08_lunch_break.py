name_of_series = input()
time_of_episode = int(input())
time_of_break = int(input())
from math import ceil

time_for_lunch = time_of_break * 1/8
time_for_chilling = time_of_break * 1/4

time_necessary = time_for_lunch + time_for_chilling + time_of_episode

if time_of_break >= time_necessary:
    print(f'You have enough time to watch {name_of_series} and left with {ceil(time_of_break - time_necessary)}'
          f' minutes free time.')
else:
    print(f"You don't have enough time to watch {name_of_series}, you need {ceil(time_necessary - time_of_break)}"
          f" more minutes.")