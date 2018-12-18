from darksky import forecast

multicampus = forecast(' 키 값', 위도, 경도)

print(multicampus['currently']['summary'])
print(multicampus['currently']['temperature'])

#import requests

#url = 'https://api.darksky.net/forecast/2e3548835d6e65079a61176c48d16428/37.501571,%20127.039638'

#res = requests.get(url)
#data = res.json()

#print(data['currently']['summary'])