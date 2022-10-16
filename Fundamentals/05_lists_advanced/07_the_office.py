list_of_score = input().split()
happiness_factor = int(input())

multiplied_score = list(map(lambda x: int(x) * happiness_factor, list_of_score))
filtered_score = list(filter(lambda a:  a >= (sum(multiplied_score) / len(list_of_score)), multiplied_score))

if len(filtered_score) < len(list_of_score) / 2:
    print(f'Score: {len(filtered_score)}/{len(list_of_score)}. Employees are not happy!')
else:
    print(f'Score: {len(filtered_score)}/{len(list_of_score)}. Employees are happy!')