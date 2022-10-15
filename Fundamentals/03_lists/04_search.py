number_of_searches = int(input())
search_word = input()
given_list = []
amended_list = []

for search_index in range(number_of_searches):
    given_word = input()
    given_list.append(given_word)
    if search_word in given_word:
        amended_list.append(given_word)

print(given_list)
print(amended_list)