import requests

url = 'https://randomuser.me/api/'
p={'results':5}
r=requests.get(url,p)
print(r.status_code)
data=r.json()
dic={}
for i in data:
    nat=data['results'][0]['nat']
    
    name=data['results'][0]['name']['first']+'_'+data['results'][0]['name']['last']
    dic.get[name]=nat
    print(dic)