city = input()
sales = float(input())
commissions = 0

if city == 'Sofia' and 0 <= sales <= 500:
    commissions = sales * 0.05
elif city == 'Sofia' and 500 <= sales <= 1000:
    commissions = sales * 0.07
elif city == 'Sofia' and 1000 <= sales <= 10000:
    commissions = sales * 0.08
elif city == 'Sofia' and sales > 10000:
    commissions = sales * 0.12

if city == 'Varna' and 0 <= sales <= 500:
    commissions = sales * 0.045
elif city == 'Varna' and 500 <= sales <= 1000:
    commissions = sales * 0.075
elif city == 'Varna' and 1000 <= sales <= 10000:
    commissions = sales * 0.1
elif city == 'Varna' and sales > 10000:
    commissions = sales * 0.13

if city == 'Plovdiv' and 0 <= sales <= 500:
    commissions = sales * 0.055
elif city == 'Plovdiv' and 500 <= sales <= 1000:
    commissions = sales * 0.08
elif city == 'Plovdiv' and 1000 <= sales <= 10000:
    commissions = sales * 0.12
elif city == 'Plovdiv' and sales > 10000:
    commissions = sales * 0.145

if commissions <= 0:
    print('error')
else:
    print(f'{commissions:.2f}')