import requests

url = 'https://randomuser.me/api/'
p={'results':2}
r=requests.get(url,p)
data=r.json()
nat=data['results'][0]['nat']
# print(r.url)
print(nat)