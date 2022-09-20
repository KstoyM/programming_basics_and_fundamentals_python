command = input()
total_tickets_for_movie = 0
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while command != 'Finish':
    name_of_movie = command
    number_of_free_spots = int(input())
    command_2 = input()
    total_tickets_for_movie = 0
    while command_2 != 'End':
        ticket_type = command_2
        total_tickets_for_movie += 1
        total_tickets += 1
        if ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'student':
            student_tickets += 1
        else:
            kid_tickets += 1

        if total_tickets_for_movie >= number_of_free_spots:
            print(f'{name_of_movie} - {total_tickets_for_movie / number_of_free_spots * 100:.2f}% full. ')
            command = input()
            break

        command_2 = input()

    else:
        print(f'{name_of_movie} - {total_tickets_for_movie / number_of_free_spots * 100:.2f}% full. ')
        command = input()
if command == 'Finish':
    print(f'Total tickets: {total_tickets}')
    print(f'{student_tickets / total_tickets * 100:.2f}% student tickets.')
    print(f'{standard_tickets / total_tickets * 100:.2f}% standard tickets.')
    print(f'{kid_tickets / total_tickets * 100:.2f}% kids tickets.')
