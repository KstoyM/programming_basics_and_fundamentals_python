first_time = int(input())
second_time = int(input())
third_time = int(input())

total_time = first_time + second_time + third_time
time_in_minutes = total_time // 60
time_in_seconds = total_time % 60

# if time_in_seconds < 10:
#     print(f'{time_in_minutes}:0{time_in_seconds}')
# else:
#     print(f'{time_in_minutes}:{time_in_seconds}')

#OR

print(f'{time_in_minutes}:{time_in_seconds:02d}')