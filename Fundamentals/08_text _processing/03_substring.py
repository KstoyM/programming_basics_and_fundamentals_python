str_for_removal = input()
work_string = input()

while str_for_removal in work_string:
    work_string = work_string.replace(str_for_removal, '')

print(work_string)
