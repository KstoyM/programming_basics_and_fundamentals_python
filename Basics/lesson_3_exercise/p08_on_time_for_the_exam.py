hour_of_exam = int(input())
minute_of_exam = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

total_min_hour_of_exam = hour_of_exam * 60
total_min_exact_exam_time = total_min_hour_of_exam + minute_of_exam
total_min_arrival_hour = arrival_hour * 60
total_min_exact_arrival_time = total_min_arrival_hour + arrival_minutes

difference = abs(total_min_exact_exam_time - total_min_exact_arrival_time)
difference_hours = difference // 60
difference_minutes = difference % 60

if total_min_exact_exam_time < total_min_exact_arrival_time and difference != 0:
    print('Late')
elif total_min_exact_exam_time >= total_min_exact_arrival_time and difference <= 30:
    print('On time')
elif total_min_exact_exam_time > total_min_exact_arrival_time and difference > 30:
    print('Early')

if total_min_exact_exam_time > total_min_exact_arrival_time and 1 <= difference <= 59:
    print(f'{difference} minutes before the start')
elif total_min_exact_exam_time > total_min_exact_arrival_time and difference >= 60:
    print(f'{difference_hours}:{difference_minutes:02d} hours before the start')
elif total_min_exact_exam_time < total_min_exact_arrival_time and difference < 60:
    print(f'{difference} minutes after the start')
elif total_min_exact_exam_time < total_min_exact_arrival_time and difference >= 60:
    print(f'{difference_hours}:{difference_minutes:02d} hours after the start')