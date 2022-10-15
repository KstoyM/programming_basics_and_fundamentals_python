number_of_searches = int(input())
search_word = input()
word_list = []

for search_index in range(number_of_searches):
    given_word = input()
    word_list.append(given_word)
print(word_list)

for search_index in range(len(word_list)-1, -1, -1):
    element = word_list[search_index]
    if search_word not in element:
        word_list.remove(element)
print(word_list)