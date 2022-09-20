user_name = input()
password = input()

user_inp_password = input()
while user_inp_password != password:
    user_inp_password = input()
print(f'Welcome {user_name}!')
