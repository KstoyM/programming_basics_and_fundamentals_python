from collections import deque

peaks = {'Vihren': 80, 'Kutelo': 90, 'Banski Suhodol': 100, 'Polezhan': 60, 'Kamenitza': 70}

food_portions = [int(el) for el in input().split(", ")]
stamina = deque([int(el) for el in input().split(", ")])

conquered_peaks = []

while peaks and food_portions:

    sum_food_stamina = food_portions.pop() + stamina.popleft()

    current_peak_name = list(peaks.keys())[0]
    current_peak_difficulty = list(peaks.values())[0]

    if sum_food_stamina >= current_peak_difficulty:
        del peaks[current_peak_name]
        conquered_peaks.append(current_peak_name)
        continue
    else:
        continue

if peaks:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
    if conquered_peaks:
        print('Conquered peaks:')
        [print(peak) for peak in conquered_peaks]
else:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK\nConquered peaks:")
    [print(peak) for peak in conquered_peaks]

