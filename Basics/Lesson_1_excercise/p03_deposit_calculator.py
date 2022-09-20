#Read Input

deposit_sum = float(input())
months = int(input())
yearly_interest_percent = float(input()) / 100

#Process input
month_gain = (deposit_sum * yearly_interest_percent) / 12
final_sum = deposit_sum + (months * month_gain)

#Pring output

print(final_sum)
