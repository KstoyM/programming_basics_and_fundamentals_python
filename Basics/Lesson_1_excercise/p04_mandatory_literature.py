#Read Input
number_of_pages_in_current_book = int(input())
pages_read_in_an_hour = int(input())
number_of_days_needed_to_read_the_book = int(input())

#Process Input

number_of_hours_needed_to_read_a_book = number_of_pages_in_current_book / pages_read_in_an_hour
number_of_hours_needed_every_day = round(number_of_hours_needed_to_read_a_book / number_of_days_needed_to_read_the_book)

#Print Output

print(number_of_hours_needed_every_day)


