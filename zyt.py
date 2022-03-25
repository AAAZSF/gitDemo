import datetime
import time

import requests
import threadpool


def daka(dic):
    today = str(datetime.date.today())
    day = int(today.split('-')[-1])
    print(day)
    print(today)
    num = dic.get('personcode')
    url = 'http://zyt.zjnu.edu.cn/H5/ZJSFDX/FillIn.aspx?address=%u6d59%u6c5f%u7701%u2730%u91d1%u534e%u5e02%u2730%u5a7a%u57ce%u533a'
    print(dic)
    session = requests.session()
    resp = session.post('http://zyt.zjnu.edu.cn/H5/Login.aspx', params={
        'UserText': num,
        'PasswordText': dic.get('password')
    })
    sessionId = session.cookies.get('ASP.NET_SessionId')
    print(sessionId)

    headers = {
        # 'Cookie': 'ASP.NET_SessionId=b0dn0tknsswhafz31w1zxcay; JKM=OK; yxkj_ticket=zPZ2ge8/ze/Sq9wvr3PjyA==; LastUserCode=202031890307; NameUser=202031890307; TimeDay=',
        # 'Cookie': 'ASP.NET_SessionId=b0dn0tknsswhafz31w1zxcay; JKM=OK; yxkj_ticket=lCl5Mt5DlstLz78+g0/dPg==; LastUserCode=202031890307; NameUser=202031890307; TimeDay=',
        'Cookie': 'Cookie: JKM=OK; ASP.NET_SessionId={sessionId}; yxkj_ticket={key}; LastUserCode={personcode}; NameUser={personcode}; TimeDay={day}'.format(
            personcode=dic['personcode'], key=dic['key'], sessionId=sessionId, day=day),

        # 'Referer': 'http://zyt.zjnu.edu.cn/H5/index/Index.htm?OP=phone_html5&r=20220305103608795',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }

    params = {
        '__EVENTTARGET': 'btn_save',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': '/wEPDwUJOTMwMDE3NjU5ZGSrucGNcWZY4gj6odekPQTFlJVeAKR3Yd2XtPjXa0w0WQ==',
        '__VIEWSTATEGENERATOR': '3674067D',
        '__EVENTVALIDATION': '/wEdABl0THonuo/+ink4LkyDZtaKnPdgn5d6iO4LuTjGeN2JM3llOAzR6kycDzMfToHX0QOa6jYEaUq7hqoikcwmGDr/nmnPxOBQ7q1ly++ofgUcfBMeg5WVSSvtrjLjx3x5POv400VKLRNp/k6261iHtmxhYdp8PLLcr00Ykm6GIg/QPm2VAoUsguAjookCWDEX54sHQe9Pfyn7J2iyftT+Cg0mL0jfXWdOZUPTgbQHBDwymb6wlsA0YdypgcCl8awhDxBgYuHAmLDqwPtQh9HDEtJjr+c7NEwFf3c5FPeYdSyrXrYIOfZQS7Mh8jWxQ/3S2fHk/wGpGPyEyYtOtvQbZ7eyCWoEiO6Dd+V6RlHl9UDOJYVHlcFqi++psAvZk9q9RG5W1pRfvYYFhXg72yYOmnpySmm9X2U2t6Y11P+J4lVyalm+n0KUg6wbhm42RvKN577lL2zWcbD6zAaEib0znaI8tWsLH8H+NXQUYD4Kkws4BfoJpIr4b0DV7eZFh6tMLUyznw6pK1ioM6RKyI7TbQybieZNWBTk3CdEPnRsq5aC3CewTWOA8Ln02pcB5hhfE24=',
        'personname': '郑顺帆',
        'personcode': '201931810335',
        'txtCreateTime': today,
        'DATA_1': '体温正常',
        'DATA_2': '正常',
        'DATA_3': '体温正常',
        'DATA_4': '否',
        'DATA_5': '绿码',
        'DATA_6': '否',
        'DATA_7': '否',
        'DATA_8': '否',
        'DATA_10': '否',
        'DATA_11': '',
        'DATA_9': '是，已经接种加强针',
        'DATA_16': '17周岁以上',
        'DATA_12': '',
        'DATA_13': '浙江师范大学本部校区',
        'DATA_14': '',
        'DATA_15': '我已知晓并如实填报',
        'hidDATA_1': '体温正常',
        'hidDATA_2': '正常',
        'hidDATA_3': '体温正常',
        'hidDATA_4': '否',
        'hidDATA_5': '绿码',
        'hidDATA_6': '否',
        'hidDATA_7': '否',
        'hidDATA_8': '否',
        'hidDATA_9': '是，已经接种加强针',
        'hidDATA_10': '否',
        'hidDATA_11': '',
        'hidDATA_12': '',
        'hidDATA_13': '浙江师范大学本部校区',
        'hidDATA_14': '',
        'hidDATA_15': '我已知晓并如实填报',
        'hidDATA_16': '17周岁以上',
        'hidDATA_17': '浙江省✰金华市✰婺城区'
            #'%u6d59%u6c5f%u7701%u2730%u91d1%u534e%u5e02%u2730%u5a7a%u57ce%u533a'
    }
    resp = session.post(url, data=params, headers=headers)
    # print(resp.text)


lst = [
    {'personname': '郑顺帆', 'personcode': '201931810335', 'key': 'zPZ2ge8/ze/Sq9wvr3PjyA==', 'password': '174810'},
    {'personname': '陈雨丹', 'personcode': '202031890307', 'key': 'lCl5Mt5DlstLz78+g0/dPg==', 'password': '202723'},
    # {'personname': '俞斯棋', 'personcode': '201931810334', 'key': 'zPZ2ge8/ze/Aon4piZGkjw==', 'password': '180012'},
    # {'personname': '尤腾毅', 'personcode': '201931810333', 'key': 'zPZ2ge8/ze+2oV/duoRyKw==', 'password': '272232'},
    # {'personname': '邱志超', 'personcode': '201931810332', 'key': 'zPZ2ge8/ze85iWApS/m0pw==', 'password': '050013'},
    # {'personname': '彭昭钰', 'personcode': '201931810331', 'key': 'zPZ2ge8/ze/+lrKHOyTMMw==', 'password': '190014'},
    # {'personname': '郑烨康', 'personcode': '201931810336', 'key': 'zPZ2ge8/ze9Xohzvzop0GA==', 'password': '254872'},
    # {'personname': '雷佳慧', 'personcode': '201931810207', 'key': 'y+x9hFCE4CyPwH2aJKvwmg==', 'password': '181826'},

]
if __name__ == '__main__':
    for i in range(2):
        for dic in lst:
            daka(dic)
