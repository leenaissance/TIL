import requests 

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)
lotto_data = response.json()

real_numbers = [
    lotto_data['drwNo'],
    lotto_data['drwtNo2'],
    lotto_data['drwtNo3'],
    lotto_data['drwtNo4'],
    lotto_data['drwtNo5'],
    lotto_data['bnusNo'],
]
print(response)

real_numbers = []

for key in lotto_data:
    print(key)


for key in lotto_data:
    if 'drwtNo' in key:
        real_numbers.append(lotto_data[key])

for key, value in lotto_data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)

real_numbers.sort()
bonus_numbers = lotto_data['bnusNo']
print(sorted(real_numbers))

"""
{
    "drwtNo6":45,
    "drwtNo4":30,
    "drwtNo5":33,
    "bnusNo":6,
    "drwtNo2":25,
    "drwtNo3":28,
    "drwtNo1":2
    }
"""