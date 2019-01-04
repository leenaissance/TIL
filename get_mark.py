t = int(input())
for i in range(1, t+1):
    numbers = input().split(' ')
    num1, num2 = int(numbers[0]), int(numbers[1])
    if num1 > num2:
        print('#', i, ' >', sep='')
    elif num1 == num2:
        print('#', i, ' =', sep='')
    elif num1 < num2:
        print('#', i, ' <', sep='')
