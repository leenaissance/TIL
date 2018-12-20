# my_numbers, real_numbers, bonus_numbers
# 1 등: my = real
# 2 등: real & my 가 5개가 같고, my 의 나머지 하나가 bonus
# 3 등: real & my 가 5개가 같다
# 4 등: real & my 가 4개가 같다
# 5 등: real & my 가 3개가 같다
# 꽝


import random
import requests

numbers = list(range(1, 46))
my_numbers = random.sample(numbers, 6)
print("my numbers :", my_numbers)


url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url)
lotto_data = response.json()

real_numbers = []
for key in lotto_data:
    if 'drwtNo' in key:
        real_numbers.append(lotto_data[key])

real_numbers.sort()
bonus_numbers = lotto_data['bnusNo']
print('real numbers : ', sorted(real_numbers))
print('bonus number : ', bonus_numbers)

"""
cnt_luck = 0
for i in my_numbers:
    if i in real_numbers:
        cnt_luck += 1

if cnt_luck == 6:
    print("1등!!!")
elif cnt_luck == 5:
    print("3등")
elif cnt_luck == 4:
    print("4등")
elif cnt_luck == 3:
    print("5등")
else:
    print("로또 한 번 더 사시죠")
"""

# # my_nubms = []
# real_numbs = []
# bnus_numbs = []
# 테스트케이스 만든 뒤 돌려보고 만들어 보는 것 추천

#교집합으로 풀어보기


inter_numbs = set(my_numbers).intersection(set(real_numbers))

if inter_numbs == set(my_numbers):
    print("1등입니다")
elif inter_numbs == set(my_numbers):
    print("3등")
    if bonus_numbers in my_numbers:
        print("2등")
elif inter_numbs == set(my_numbers):
    print("4등")
elif inter_numbs == set(my_numbers):
    print("5등")
else:
    print("꽝!")


# 해설
#1번 방법
count = 0
for my_number in my_numbers:
    for real_number in real_numbers:
        if my_number == real_number:
            count += 1

if count == 6:
    print(1)
elif count == 5 and bonus_numbers in my_numbers:
    print(2)
elif count == 5:
    print(3)
elif count == 4:
    print(4)
elif count == 3:
    print(5)
else:
    print("ㅠㅠ")

# #2번 방법
# list = [1, 2, 3]
# tuple = (1, 2, 3)
# set = {1, 2, 3} 순서가 없다 / 요소가 있는지는 물어볼 수 있다

my_numbers = set(my_numbers)
real_numbers = set(real_numbers)
match_count = len(my_numbers & real_numbers)

