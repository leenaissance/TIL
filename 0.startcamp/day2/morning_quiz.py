#1. 평균을 구하시오
#type 은 float

my_score = [79 ,84, 66, 93]
my_average = sum(my_score) / len(my_score) # iterable : 돌 수만 있으면 동작함
print("my average : ", my_average)

"""
for i in my_score:
    i = (i+i)/len(my_score)
    print(i)
"""

your_score = {
    '수학' : 87,
    '국어' : 83,
    '영어' : 76,
    '도덕' : 100,
}

numbs = your_score.values() # 이 값은 리스트? 무슨 type일까
your_average = sum(numbs) / len(numbs)
print("your average : ", your_average) # UX디자이너가 하는 일!

cities_temp = {
    '서울' : [-6, -10, 5],
    '대전' : [-3, -5, 2],
    '광주' : [0, -5, 10],
    '구미' : [2, -2, 9],
}


"""
3: 도시별 온도 평균
서울: '?'
대전: '?'
광주: '?'
구미: '?'

av_seoul_temp = round((sum(cities_temp['서울']) / len(cities_temp['서울'])),1)
av_Dae_temp = round((sum(cities_temp['대전']) / len(cities_temp['대전'])), 1)
av_Kwang_temp = round((sum(cities_temp['광주']) / len(cities_temp['광주'])), 1)
av_Koo_temp = round((sum(cities_temp['구미']) / len(cities_temp['구미'])),1)

print(" 서울: ", av_seoul_temp,"\n", "대전: ", av_Dae_temp, "\n", "광주: ", av_Kwang_temp, "\n", "구미: ", av_Koo_temp)

"""

#3번 해설
# dict.items 튜플? 셋?
#.itms()를 붙이면 키, 밸류를 같이 꺼낼 수 있다

#양손으로 둘 다 꺼내요
for city, temperatures in cities_temp.items():
    print(city + " : " + str(sum(temperatures) / len(temperatures)))

# 왼손으로 key만 꺼내요 
for city in cities_temp:
    temperatures = cities_temp[city]
    avg_temperature = round(sum(temperatures) / len(temperatures), 2)
    print(city + " : " + str(avg_temperature))

# for city in cities_temp:
#     print(city)
#     print(cities_temp[city])

# 문자열 + 문자열 (덧셈연산 O) / 문자열 + 정수or실수 (덧셈연산 X) -> 수를 srt()로 타입캐스팅
# 타입캐스팅 하지 않고 하는 법 -> print('{}: {}'.format(city, avg_temperature))
