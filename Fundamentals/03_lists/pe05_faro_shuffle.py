cards_received = input().split()
swaps = int(input())
left_deck = []
right_deck = []
deck_separator = len(cards_received) // 2

for card in range(0, deck_separator):
    left_deck.append(cards_received[card])

for card in range(deck_separator, len(cards_received)):
    right_deck.append(cards_received[card])

for swap in range(swaps):
    final_deck = []
    for card_index in range(len(left_deck)):
        final_deck.append(left_deck[card_index])
        final_deck.append(right_deck[card_index])

    cards_received = final_deck

print(final_deck)