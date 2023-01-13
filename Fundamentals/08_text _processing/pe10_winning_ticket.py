tickets = [ticket.strip() for ticket in input().split(", ")]

for ticket in tickets:
    left_half = ticket[0: int(len(ticket) / 2)]
    right_half = ticket[int(len(ticket) / 2): int(len(ticket))]

    if int(len(ticket)) == 20:
        winning_symbols = ['@', '#', '$', '^']

        for match_symbol in winning_symbols:
            for uninterrupted_match_length in range(10, 5, -1):
                winning_symbol_repetitions = match_symbol * uninterrupted_match_length
                if winning_symbol_repetitions in left_half and winning_symbol_repetitions in right_half:
                    if uninterrupted_match_length == 10:
                        print(f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!')
                    else:
                        print(f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}')

                else:
                    print(f': "ticket "{ticket}" - no match"')

    else:
        print("invalid ticket")
