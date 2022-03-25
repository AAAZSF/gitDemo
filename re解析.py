import requests
import re
import csv


def get(url, headers, param):
    resp = requests.get(url, headers=headers, params=param)
    text = resp.text
    obj = re.compile(
        r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<br>(?P<year>.*?)&nbsp.*?<span>(?P<num>.*?)人评价</span>',
        re.S)

    res = obj.finditer(text)
    resp.close()
    return res


url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/98.0.4758.81 Safari/537.36 '
}
param = {
    'start': '',
    'filter': ''
}

f = open('top250.csv', mode='w+', encoding='gbk', newline='')
writer = csv.writer(f)
flag = 1
for start in range(0, 250, 25):
    param['start'] = start
    res = get(url, headers, param)
    for i in res:
        dict = i.groupdict()
        dict['year'] = dict['year'].strip()
        print(dict.values())
        if flag == 1:
            writer.writerow(dict.keys())
            flag = 0
        writer.writerow(dict.values())

f.close()
