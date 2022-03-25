# coding=UTF-8
import requests
import re
def getToken():
    url = 'http://zwgl.zjnu.edu.cn/Api/auto_user_check'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'
    }
    params = {
        'user': '202030140323',
        'p': '728f154fd3469c47fc605bd0ca9697de',
        'callback': 'http://zwgl.zjnu.edu.cn/home/web/seat/area/1'
    }
    resp=requests.get(url,headers=headers,params=params)
    print(resp.headers)
    obj = re.compile(
            r'access_token=(?P<token>.*?);',
            re.S)
    print(resp.headers.get('Set-Cookie'))
    res=obj.finditer(resp.headers.get('Set-Cookie'))

    for i in res:
        token=i.groupdict().get('token')
    return token

token=getToken()
print(token)

headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
}
flag=0
for i in range(4407,4647):
    for j in range(0,1000):
        data1 = {
            'access_token': token,
            'userid': '202030140323',
            'segment': str(1304300+j),
            'type': '1',
            'operateChannel': '2'
        }
        url1="http://zwgl.zjnu.edu.cn/api.php/spaces/"+str(i)+"/book"
        ans = requests.post(url=url1,headers=headers1,data=data1)
        if ans.text.find('预约成功')!=-1:
            print('预约成功 数字资源学习空间'+str(i-4407+1)+'号座位')
            flag=1
        #print(ans.json())
if flag==0:
    print('没抢到？不可能吧，快联系ftx调代码！')
