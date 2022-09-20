cnt_of_purchased_chrysanthemum = int(input())
cnt_of_purchased_roses = int(input())
cnt_of_purchased_tulips = int(input())
season = input()
holiday = input()
discount = 0

if season == 'Spring' or season == 'Summer':
    price_of_chrys = 2
    price_of_roses = 4.1
    price_of_tulips = 2.5
else:
    price_of_chrys = 3.75
    price_of_roses = 4.5
    price_of_tulips = 4.15

total_price = price_of_chrys * cnt_of_purchased_chrysanthemum + price_of_roses * cnt_of_purchased_roses\
              + price_of_tulips * cnt_of_purchased_tulips

if holiday == 'Y':
    total_price *= 1.15

if cnt_of_purchased_tulips > 7 and season == 'Spring':
    discount += total_price * 0.05
if cnt_of_purchased_roses >= 10 and season == 'Winter':
    discount += (total_price - discount) * 0.1
if cnt_of_purchased_roses + cnt_of_purchased_tulips + cnt_of_purchased_chrysanthemum > 20:
    discount += (total_price - discount) * 0.2

price_of_all_flowers = total_price - discount + 2
print(f'{price_of_all_flowers:.2f}')