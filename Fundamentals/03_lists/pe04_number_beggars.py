money_for_beggars = input().split(', ')
count_of_beggars = int(input())

final_money = []
starting_index = 0
money_list_as_digit = []
for element in money_for_beggars:
    money_list_as_digit.append(int(element))

while starting_index < count_of_beggars:
    current_beggar_money = 0
    for money_for_beggar in range(starting_index, len(money_for_beggars), count_of_beggars):
        current_beggar_money += money_list_as_digit[money_for_beggar]
    starting_index += 1
    final_money.append(current_beggar_money)

print(final_money)