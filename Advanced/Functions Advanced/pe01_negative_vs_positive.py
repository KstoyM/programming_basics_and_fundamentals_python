def print_result(positive, negative):
    print(negative)
    print(positive)

    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]
positive_numbers = sum(n for n in numbers if n > 0)
negative_numbers = sum(n for n in numbers if n < 0)

print_result(positive_numbers, negative_numbers)