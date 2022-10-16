first_list = input().split(', ')
second_list = input().split(', ')
# result_list = []
# for word in first_list:
#     for word1 in second_list:
#         if word in word1:
#             if word not in result_list:
#                 result_list.append(word)
#
# print(result_list)

substrings = [first for first in first_list if any(first in second for second in second_list)]
print(substrings)