import requests

url = 'https://music.163.com/weapi/comment/resource/comments/get'
# data = {
#     'params': 'DQ0HSJFtGHKFFxLKvUK7t0ITRfphv31BUMVA9acZ1WbWMBMNJ+HZZ5qOaBIfxLWKgyn1l6k6N9lXdjJ8aTVxXcOfsGsP+oAp6/V6XbEnCBCv/I9Qq4AdJTGbU9CDI/ofp4LYoschHx83xzDYBktBiZDdzzRyA5H3FQjTwqdNNqaKFl/YM0/u/PufMjK9bGEOTO3wOqy6xpQDhbVhzqrTWDCow48Twyvn8zNUqMGyD46WMHyMXBM4xyHLsV/fxSh7kvYupRzVOXGendB2CjNrzhG5UhqBsYmEkDmnWavJwa8=',
#     'encSecKey': '8d76dbddd5b31a0b78d17305c36b793d83c806114ec093d11fd5d69e621cd5fc98d53bf47c9a3d781a34846a057ea4527d823bac5c84080568567c8b891fb2fb89131c2ac69b251fcca592f6672a3a6e425109d9005534f559258b785793d63aead8bd5e41599b5c06308283892988428e8bb15c3025f36037dd3bf7cc82daad'
# }
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1901371647",
    "threadId": "R_SO_4_1901371647"
}
# !function() {
#     function a(a) {
#         var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
#         for (d = 0; a > d; d += 1)
#             e = Math.random() * b.length,
#             e = Math.floor(e),
#             c += b.charAt(e);
#         return c
#     }
#     function b(a, b) {
#         var c = CryptoJS.enc.Utf8.parse(b)
#           , d = CryptoJS.enc.Utf8.parse("0102030405060708")
#           , e = CryptoJS.enc.Utf8.parse(a)
#           , f = CryptoJS.AES.encrypt(e, c, {
#             iv: d,
#             mode: CryptoJS.mode.CBC
#         });
#         return f.toString()
#     }
#     function c(a, b, c) {
#         var d, e;
#         return setMaxDigits(131),
#         d = new RSAKeyPair(b,"",c),
#         e = encryptedString(d, a)
#     }
#     function d(d, e, f, g) {   d:data.json  e:010001 f:00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7
#         g : 0CoJUm6Qyw8W8jud
#         var h = {}
#           , i = a(16);
#         return h.encText = b(d, g),
#         h.encText = b(h.encText, i),
#         h.encSecKey = c(i, e, f),
#         h
#     }
#     function e(a, b, d, e) {
#         var f = {};
#         return f.encText = c(a + e, b, d),
#         f
#     }
#     window.asrsea = d,
#     window.ecnonasr = e
# }();
resp = requests.post(url, data=data)
print(resp.json()['data']['hotComments'][0]['content'])
