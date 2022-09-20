pepys_budget = float(input())
number_of_gpu = int(input())
number_of_cpu = int(input())
number_of_ram = int(input())

gpu_price = 250 * number_of_gpu
cpu_price = gpu_price * 0.35 * number_of_cpu
ram_price = gpu_price * 0.1 * number_of_ram
price_of_all = gpu_price + cpu_price + ram_price


if number_of_gpu > number_of_cpu:
    price_of_all = price_of_all - (price_of_all * 0.15)

if price_of_all <= pepys_budget:
    print(f'You have {pepys_budget - price_of_all:.2f} leva left!')
else:
    print(f'Not enough money! You need {price_of_all - pepys_budget:.2f} leva more!')