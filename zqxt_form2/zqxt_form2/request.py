import requests

url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET'
r = requests.get(url.replace('APPID', 'wx0287825317d8052e')
                    .replace('APPSECRET', '52714a5e843d7bfbe295b5e5467d9c07'))
print(r.text)
