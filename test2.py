import json
import re

import requests
from Crypto.Cipher import AES
from base64 import b64encode

session = requests.session()


def getKey():  # 获取密钥
    url = 'http://authserver.zjnu.edu.cn/authserver/login'
    resp = session.get(url,headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
    })
    resp.encoding = 'utf-8'
    obj = re.compile(r'id="pwdDefaultEncryptSalt" value="(?P<key>.*?)"/>', re.S)
    res = obj.findall(resp.text)
    obj2 = re.compile(r'name="lt" value="(?P<lt>.*?)"/>', re.S)
    res = obj.findall(resp.text)
    res2 = obj2.findall(resp.text)

    return {'key': res[0], 'lt': res2[0]}


def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


# "3w7sbAcy8Xmrtchp"
def getPwd(data, key):
    key = key.strip()
    rds64 = "E8B5Pk3AXaKQhmaeSF6QR6AzAC3MPpZpT6b2Ark8bWtXpHMFKF3JTk5GQQ7PxjfZ"
    rds16 = "xZB4KPhKGbQMFtp8"
    print(rds64 + data, key)
    data = to_16(rds64 + data)

    aes = AES.new(key=key.encode('utf-8'), IV=rds16.encode('utf-8'), mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode('utf-8'))
    print(str(b64encode(bs), 'utf-8'))
    return str(b64encode(bs), 'utf-8')


def login(pwd, lt):
    url = 'http://authserver.zjnu.edu.cn/authserver/login?service=http%3A%2F%2Fzwgl.zjnu.edu.cn%2Fcas%2Findex.php%3Fcallback%3Dhttp%3A%2F%2Fzwgl.zjnu.edu.cn%2Fhome%2Fweb%2Fseat%2Farea%2F1'
    # url = 'http://authserver.zjnu.edu.cn/authserver/login?service=http://zwgl.zjnu.edu.cn/cas/index.php?callback=http://zwgl.zjnu.edu.cn/home/web/seat/area/1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
    }
    data = {
        'username': '201931810335',
        'password': pwd,
        'lt': lt,
        'dllt': 'userNamePasswordLogin',
        'execution': 'e1s1',
        '_eventId': 'submit',
        'rmShown': '1'
    }
    print(data)
    resp = session.post(url, headers=headers, data=data)
    print(resp.request.url)
    print(resp.request.headers)
    print(resp.headers)


if __name__ == '__main__':
    res = getKey()
    key, lt = res['key'], res['lt']
    pwd = getPwd(data='ZSFQQ63416261+.', key=key)
    login(pwd, lt)
