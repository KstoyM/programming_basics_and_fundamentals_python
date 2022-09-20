password_entered_by_user = input()
correct_password = 's3cr3t!P@ssw0rd'

if password_entered_by_user == correct_password:
    print('Welcome')
else:
    print(f'Wrong password!')
