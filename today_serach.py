import requests
from bs4 import BeautifulSoup

url ='https://www.naver.com' 

response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

data_set = soup.select('.ah_k')
data = data_set

