num1 = int(input())
num2 = int(input())

divisor_num1 = []
divisor_num2 = []
for i in range(1, num1+1, 1):
    if num1 % i == 0:
        divisor_num1.append(i)
for i in range(1, num2+1, 1):
    if num2 % i == 0:
        divisor_num2.append(i)
for gcd in divisor_num1:
    if gcd in divisor_num2:
        greatest_common_divisor = gcd
print(greatest_common_divisor)
    
# 10과 15를 소인수 분해한다? 1부터 시작해서 n까지 나머지가 0이 되게 나누는 수를 구한다
# l_n1을 돌면서 ㅣ_n2와 일치하는 수 중 제일 큰 수를 구한다
# 두 수를 곱하고 최대공약수로 나눈다

least_common_multiple = num1*num2 // greatest_common_divisor
print(least_common_multiple)