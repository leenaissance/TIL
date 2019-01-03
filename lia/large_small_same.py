t = int(input())
for i in range(1, t + 1):
    numbers = input().split(' ')
    number1, number2 = numbers[0], numbers[1]
    if number1 > number2:
        result = ">"
    elif number1 == number2:
        result = "="
    else:
        result = "<"
# number1, number2 = int(numbers[0]), int(numbers[1])
# 입력만 먼저 다 받고, 출력은 뒤에 해야 하는건가?

print("#", i, result)