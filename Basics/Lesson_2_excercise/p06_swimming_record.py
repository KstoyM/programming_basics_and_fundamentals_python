from math import floor
previous_record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_needed_for_one_meter = float(input())

resistance = floor(distance_in_meters / 15)
resistance *= 12.5

time_of_ivancho = distance_in_meters * time_in_seconds_needed_for_one_meter + \
            resistance

if time_of_ivancho < previous_record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {time_of_ivancho:.2f} seconds.')
else:
    print(f'No, he failed! He was {time_of_ivancho-previous_record_in_seconds:.2f} seconds slower.')