import requests
from bs4 import BeautifulSoup
from random import sample, choice

# url = 'https://movie.naver.com/movie/running/current.nhn'
# response = requests.get(url).text
# soup = BeautifulSoup(response,'html.parser')
# data_set = soup.select('.tit')
# # print(data_set)

# movie_list = []
# for data in data_set:
#     data_len = len(movie_list)
#     movie_list.append(data.text)
#     #print(choice(movie_list))
# print(sample(movie_list, 1))

def movie_want():
    url = 'https://movie.naver.com/movie/running/current.nhn'
    response = requests.get(url).text
    soup = BeautifulSoup(response,'html.parser')
    data_set = soup.select('.tit')
    movie_list = []
    for data in data_set:
        movie_list.append(data.text.replace('\n', '**'))
    return sample(movie_list, 1)

a = movie_want()
print(a)

# movie_list.append( data.txt.replace('\n', '') )