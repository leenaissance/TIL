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


url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)
lotto_data = response.json()

real_numbers = []
for key in lotto_data:
    if 'drwtNo' in key:
        real_numbers.append(lotto_data[key])

        real_numbers.sort()
bonus_numbers = lotto_data['bnusNo']
print('real numbers : ', sorted(real_numbers))
print('bonus number : ', bonus_numbers)

cnt_luck = 0
for i in my_numbers:
    if i in real_numbers:
        cnt_luck += 1

if cnt_luck == 6:
    print("1등!!!")
elif cnt_luck == 5:
    print("3등")
    # if bonus_numbers in my_numbers:
    #     print("2등")
elif cnt_luck == 4:
    print("4등")
elif cnt_luck == 3:
    print("5등")
else:
    print("로또 한 번 더 사시죠")

# # my_nubms = []
# real_numbs = []
# bnus_numbs = []
# 테스트케이스 만든 뒤 돌려보고 만들어 보는 것 추천