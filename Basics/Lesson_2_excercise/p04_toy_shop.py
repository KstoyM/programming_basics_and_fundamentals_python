price_of_the_trip = float(input())
number_of_puzzles = int(input())
number_of_talking_toys = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_truck = int(input())

puzzle = 2.6
talking_toy = 3
teddy_bear = 4.1
minion = 8.2
truck = 2

price_of_all_toys = number_of_puzzles * puzzle + number_of_talking_toys * talking_toy + \
                    number_of_teddy_bears * teddy_bear + number_of_minions * minion + \
                    number_of_truck * truck

number_of_toys = number_of_talking_toys + number_of_truck + number_of_minions + \
                 number_of_puzzles + number_of_teddy_bears

if number_of_toys >= 50:
    price_of_all_toys = price_of_all_toys - (price_of_all_toys * 0.25)
    money_won = price_of_all_toys - (price_of_all_toys*0.1)
else:
    money_won = price_of_all_toys - (price_of_all_toys*0.1)

remaining_funds = money_won - price_of_the_trip
needed_funds = price_of_the_trip - money_won

if remaining_funds >= 0:
    print(f'Yes! {remaining_funds:.2f} lv left.')
else:
    print(f'Not enough money! {needed_funds:.2f} lv needed.')
