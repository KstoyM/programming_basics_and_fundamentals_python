#Read Input
yearly_basketball_price = int(input())

#Process Input

price_of_shoes = yearly_basketball_price - (yearly_basketball_price * 0.4)
price_of_uniform = price_of_shoes - (price_of_shoes * 0.2)
price_of_ball = price_of_uniform - (price_of_uniform * 0.75)
price_of_accessories = price_of_ball - (price_of_ball * 0.8)

total_price = price_of_accessories + price_of_uniform + price_of_ball + price_of_shoes + yearly_basketball_price

#Print Output
print(total_price)