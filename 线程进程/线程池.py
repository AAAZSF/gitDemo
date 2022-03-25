import requests

url = 'http://xinfadi.com.cn/getCat.html'
resp = requests.post(url, params={'prodCatid': '1188'})
res=resp.json()['list'][0]['id']
print(res)
dict
