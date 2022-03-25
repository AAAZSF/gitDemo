import requests
from lxml import etree


def a():
    url = 'https://beijing.zbj.com/search/f'
    param = {'kw': 'saas'}
    resp = requests.get(url, params=param)
    resp.encoding = 'utf-8'
    html = etree.HTML(resp.text)
    resp.close()
    divs = html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')
    # print(divs)
    for div in divs:
        price = div.xpath('./div/div/a[2]/div[2]/div[1]/span[1]/text()')[0].strip('¥')
        title = 'SAAS'.join(div.xpath('./div/div/a[2]/div[2]/div[2]/p/text()'))
        name = div.xpath('./div/div/a[1]/div[1]/p/text()[2]')[0].strip()
        location = div.xpath('./div/div/a[1]/div[1]/div/span/text()')[0]

        yield price, title, name, location


for i in a():
    print(i)
