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

for key in lotto_data:
    if 'drwtNo' in key:
        real_numbers.append(lotto_data[key])

        real_numbers.sort()
bonus_numbers = lotto_data['bnusNo']
print('real numbers : ', sorted(real_numbers))