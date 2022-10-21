targets = list(map(int, input().split()))

command = input()
shot_targets = 0

while True:

    if command == "End":
        break

    curr_index = int(command)
    if curr_index >= len(targets) or curr_index < 0:
        command = input()
        continue
    else:
        current_target = targets.pop(curr_index)
        if current_target == -1:
            command = input()
            continue
        else:
            for element in targets:
                if element > current_target and element != -1:
                    element_index = targets.index(element)
                    element = targets.pop(element_index)
                    element -= current_target
                    targets.insert(element_index, element)
                elif element <= current_target and element != -1:
                    element_index = targets.index(element)
                    element = targets.pop(element_index)
                    element += current_target
                    targets.insert(element_index, element)
        shot_targets += 1
        current_target = -1
        targets.insert(curr_index, current_target)
        command = input()

print(f"Shot targets: {shot_targets} -> {' '.join(str(target) for target in targets)}")
