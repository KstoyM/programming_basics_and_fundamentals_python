n_tabs_open = int(input())
salary = int(input())

for n in range(n_tabs_open):
    current_tab = input()
    if current_tab == 'Facebook':
        salary -= 150
    elif current_tab == 'Instagram':
        salary -= 100
    elif current_tab == 'Reddit':
        salary -= 50
    if salary <= 0:
        print('You have lost your salary.')
        break
if salary > 0:
    print(f'{salary}')
