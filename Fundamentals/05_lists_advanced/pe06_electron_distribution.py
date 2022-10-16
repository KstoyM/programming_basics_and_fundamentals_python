electrons = int(input())
shell_list = []
position = 1

while True:

    if electrons == 0:
        break

    current_shell = 2 * position ** 2
    if electrons >= current_shell:
        shell_list.append(current_shell)
        position += 1
        electrons -= current_shell
    else:
        shell_list.append(electrons)
        electrons = 0

print(shell_list)