command = input()

prime_numbers = 0
non_prime_numbers = 0
flag = False

while command != 'stop':
    curr_number = int(command)

    if curr_number < 0:
        print('Number is negative.')
        command = input()
        continue

    for n in range(2, curr_number):
        if curr_number % n == 0:
            flag = True
            break
    if flag:
        non_prime_numbers += curr_number
    else:
        prime_numbers += curr_number
    flag = False
    command = input()

print(f"Sum of all prime numbers is: {prime_numbers}")
print(f"Sum of all non prime numbers is: {non_prime_numbers}")
