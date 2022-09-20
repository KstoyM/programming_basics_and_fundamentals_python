user_input = float(input())

# 26.00 - 35.00	Hot
# 20.1 - 25.9	Warm
# 15.00 - 20.00	Mild
# 12.00 - 14.9	Cool
# 5.00 - 11.9	Cold


if user_input > 35:
    print("unknown")
elif user_input < 5:
    print('unknown')
elif user_input <= 11.9:
    print('Cold')
elif user_input <= 14.9:
    print('Cool')
elif user_input <= 20:
    print('Mild')
elif user_input <= 25.9:
    print("Warm")
elif user_input <= 35:
    print("Hot")

