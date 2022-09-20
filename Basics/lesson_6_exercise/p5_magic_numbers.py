num = int(input())

for thousands in range(1, 10):
    for hundreds in range(1, 10):
        for tens in range(1, 10):
            for ones in range(1, 10):
                if num % thousands == 0 and num % hundreds == 0 \
                        and num % tens == 0 and num % ones == 0:
                    print(f'{thousands}{hundreds}{tens}{ones} ', end='')