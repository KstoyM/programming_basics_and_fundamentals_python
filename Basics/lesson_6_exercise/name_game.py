best_player_name = ''
total_sum = 0
final_sum = 0

while True:
    name = input()

    if name == 'Stop':
        break

    for ch in name:
        current_number = int(input())

        if current_number == ord(ch):
            total_sum += 10
        else:
            total_sum += 2

    if total_sum > final_sum:
        final_sum = total_sum
        best_player_name = 'name'

print(f'The winner is {best_player_name} with {final_sum} points!')

    total_sum = 0