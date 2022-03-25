import datetime
import json
import re
import time
import tkinter
import tkinter.messagebox

import requests


def getToken():
    url = 'http://zwgl.zjnu.edu.cn/Api/auto_user_check'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
    }
    params = {
        'user': userid,
        'p': p,
        'callback': 'http://zwgl.zjnu.edu.cn/home/web/f_second'
    }
    # params = {
    #     'user': '202031990118',
    #     'p': 'bf7956608c3fd838d9119eafef02f8af',
    #     'callback': 'http://zwgl.zjnu.edu.cn/home/web/f_second'
    # }
    resp = requests.get(url, headers=headers, params=params)
    obj = re.compile(
        r'access_token=(?P<token>.*?);',
        re.S)
    res = obj.finditer(resp.headers.get('Set-Cookie'))

    for i in res:
        token = i.groupdict().get('token')
    print(token)
    return token


def getSegment():
    url = 'http://zwgl.zjnu.edu.cn/api.php/v3areadays/15'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    # print(resp.json())
    return resp.json()['data']['list'][0]['id']


def getEmptyPlace(segment):
    url = 'http://zwgl.zjnu.edu.cn/api.php/spaces_old'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
    }
    params = {
        'area': '15',
        'segment': segment,
        'day': time.strftime('%Y-%m-%d', time.localtime(time.time())),
        'startTime': time.strftime('%H:%M', time.localtime(time.time())),
        'endTime': '23:00'
    }
    lst = requests.get(url, headers=headers, params=params).json()['data']['list']
    for i in lst:
        if i['status'] == 1:
            return i['id']


def gogogo(token, segment, seatNum):
    url = 'http://zwgl.zjnu.edu.cn/api.php/spaces/{seatNum}/book'.format(seatNum=seatNum)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
    }
    print(url)
    params = {
        'access_token': token,
        'userid': userid,
        'segment': segment,
        'type': '1',
        'operateChannel': '2'
    }
    # print(params)

    resp = requests.post(url, headers=headers, params=params)
    print(resp.json())
    return resp.json()


if __name__ == '__main__':
    userid = '201931810335'
    p = 'a8b69f51d0b98b03e1977e6dfd6433fe'
    token = getToken()
    segment = getSegment()
    while 1:
        emptyPlace = getEmptyPlace(segment)
        if emptyPlace != None:
            res = gogogo(token, segment, emptyPlace)
            print(res['msg'])
            print(res['status'])
            if res['status'] == 1:
                root = tkinter.Tk()
                root.wm_attributes('-topmost', 1)
                tkinter.messagebox.showinfo('提示', '成功抢到位置')
                break
            elif res['status'] == 6:
                print('居然没抢到？')
            tkinter.messagebox.showinfo('提示', '奇怪的错误')
            break

        else:
            print('暂时无空位')
        time.sleep(1)

    # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
