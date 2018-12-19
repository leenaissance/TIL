cities_temp = {
    '서울' : [-6, -10, 5],
    '대전' : [-3, -5, 2],
    '광주' : [0, -5, 10],
    '구미' : [2, -2, 9],
}

#4번 해설
# 1번 방식) : hot = -100 / cold = 100 기준값 선언하고 비교한다

#2번 방식) :
#all_temp에 모든 기온을 모은다
all_temp = []
for key, value in cities_temp.items():
    all_temp += value

print(all_temp)
#all_temp에서 최대 최소를 찾는다
Highst = max(all_temp)
Lowest = min(all_temp)
print(Highst, Lowest)
#cities_temp에서 최대가 든 도시를 찾고, 최소가 든 도시를 찾는다
for key, value in cities_temp.items():
    if Highst in value:
        print("Hottest : ", key)
    if Lowest in value:
        print("Coldest : ", key)


문자열로 만들기
hottest = ''
lowest = ''

hottest = key
lowest = key
print(hottest, lowest)




리스트로 만들기
hottest = []
lowest = []

hottest.append(key)
lowest.append(key)
print(hottest, lowest)

"""
4: 도시중에 최근 3일간 가장 추웠던 곳, 가장 더웠던 곳
리스트에서 가장 작은 값 min / 가장 큰 값 max
리스트끼리 비교
리스트 안의 최저값끼리 비교 / 리스트 안의 최대값끼리 비교
리스트 안의 값 비교
밸류값으로 키값 반환
Hottest: ??, Coldest: ??

temp_list = cities_temp.values()
for i in temp_list:
    if i == min(temp_list):
        print(i)
"""

# #원형's advice
# for city, temper in cities_temp:
#     max_temp = max(cities_temp)
#     if max(temper) == max_temp:
#         print(city)


# max_temp = -1000
# for city, temp_list in cities_temp:
#     if max_temp < max(temp_list):
#         max_temp = max(temp_list)
#         max_city = city

# print(max_city, max_temp)