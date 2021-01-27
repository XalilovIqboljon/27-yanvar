import requests

headers={'X-Api-Key':'f6ee3c0e1e3148469afadf1793e2fb35'}
url='https://randommer.io/api/Card'
r=requests.get(url,headers=headers)
print(r.url)