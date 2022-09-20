fav_book = input()
books_cnt = 0
is_found = False

curr_book = input()

while curr_book != 'No More Books':

    if curr_book == fav_book:
        is_found = True
        break

    books_cnt += 1
    curr_book = input()

if is_found:
    print(f'You checked {books_cnt} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {books_cnt} books.')