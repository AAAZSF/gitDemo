import datetime
import time

import requests

import tkinter
import tkinter.messagebox


def getNum():
    headers = {
        'Host': 'zwgl.zjnu.edu.cn',
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2012K11AC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3189 MMWEBSDK/20220105 Mobile Safari/537.36 MMWEBID/9683 MicroMessenger/8.0.19.2080(0x2800133B) Process/toolsmp WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
        'Origin': 'http://www.skalibrary.net',
        'X-Requested-With': 'com.tencent.mm',
        'Referer': 'http://www.skalibrary.net/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    date = str(datetime.datetime.now().date())
    params = {
        'date': date
    }

    url = 'http://zwgl.zjnu.edu.cn/api.php/v3areas'
    resp = requests.get(url, headers=headers, params=params)
    lst = resp.json()['data']['list']['childArea']

    s = '数字'
    # s = '多媒体'

    res = [{'地点': place.get('name'), '剩余位置': place.get('TotalCount') - place.get('UnavailableSpace')} for place in lst
           if
           place['name'].count(s) != 0]
    print(res)
    return res[0]['剩余位置']


while getNum() <= 0:
    time.sleep(3)




