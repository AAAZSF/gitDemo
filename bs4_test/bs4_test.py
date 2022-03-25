import requests
from bs4 import BeautifulSoup


def download(url, name):
    img_resp = requests.get(url)
    with open('img/'+name + '.jpg', mode='wb') as f:
        f.write(img_resp.content)
    print('over', name)
    img_resp.close()


url = 'https://sc.chinaz.com/tupian/fengjing.html'
resp = requests.get(url)
resp.encoding = 'utf-8'
main = BeautifulSoup(resp.text, features='html.parser')
alst = main.find('div', class_='clearfix psdk imgload').findAll('a')
sub_urls = set()
resp.close()
for i in alst:
    href = i.get('href')
    lst = href.split('.')
    if lst[-1] == 'htm':
        sub_urls.add('https:' + href)

for sub_url in sub_urls:
    sub_resp = requests.get(sub_url)
    sub_resp.encoding = 'utf-8'
    sub = BeautifulSoup(sub_resp.text, features='html.parser')
    imga = sub.find('div', class_='imga')
    download('https:' + imga.find('img').get('src'), imga.find('a').get('title'))
    sub_resp.close()
print('allover')
