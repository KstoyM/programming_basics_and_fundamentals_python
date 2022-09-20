pool_volume_liters = int(input())
hourly_debit_first_pipe = int(input())
hourly_debit_second_pipe = int(input())
hours_break_employee = float(input())

amount_filled = (hourly_debit_first_pipe + hourly_debit_second_pipe) * hours_break_employee
amount_filled_percentage = (hourly_debit_first_pipe + hourly_debit_second_pipe) * hours_break_employee / pool_volume_liters
pipe_one_percentage = hourly_debit_first_pipe * hours_break_employee / amount_filled
pipe_two_percentage = hourly_debit_second_pipe * hours_break_employee / amount_filled

if amount_filled <= pool_volume_liters:
    print(f'The pool is {amount_filled_percentage * 100:.2f}% full. Pipe 1:'
          f' {pipe_one_percentage * 100:.2f}%. Pipe 2: {pipe_two_percentage * 100:.2f}%."')
else:
    print(f'For {hours_break_employee:.2f} hours the pool overflows with {amount_filled - pool_volume_liters:.2f} liters.')