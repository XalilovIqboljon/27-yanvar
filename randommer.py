import requests

headers={'X-Api-Key':'f6ee3c0e1e3148469afadf1793e2fb35'}
url='https://randommer.io/api/Card'
payload={
    "type":"Visa"
}
r=requests.get(url,params=payload, headers=headers)
print(r.url)
print(r.json())