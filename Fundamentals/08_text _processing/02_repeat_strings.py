words = input().split()
result_list = []
for word in words:
    word *= len(word)
    result_list.append(word)
print(''.join(result_list))
