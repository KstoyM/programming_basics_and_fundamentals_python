from collections import deque


def print_func():
    if word_found:
        print(f'Word found: {key}')
    else:
        print('Cannot find any word!')
    if vowels:
        print(f'Vowels left: {" ".join(vowels)}')
    if consonants:
        print(f'Consonants left: {" ".join(consonants)}')
    quit()


vowels = deque(input().split(" "))
consonants = input().split(" ")
word_found = ''
flowers_dict = {"rose": [], "tulip": [], "lotus": [], "daffodil": []}

while vowels and consonants:

    curr_vow = vowels.popleft()
    curr_cons = consonants.pop()

    for key, value in flowers_dict.items():

        if curr_vow in key:
            flowers_dict[key].append(curr_vow)
            if len(key) == len(set(value)):
                word_found = key
                print_func()

        if curr_cons in key:
            flowers_dict[key].append(curr_cons)
            if len(key) == len(set(value)):
                word_found = key
                print_func()

else:
    print_func()
