def perf_number(num):
    sum_numbers = 0
    for index in range(1, (num // 2) + 1):
        if num % index == 0:
            sum_numbers += index
    if sum_numbers == num:
        return True


input_number = int(input())
if perf_number(input_number):
    print('We have a perfect number!')
else:
    print("It's not so perfect.")