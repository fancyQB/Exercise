import requests

#通过requests创建一个会话
session = requests.Session()

url ='https://cn.bing.com/translator/'


headers = {

    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
#发送了一个请求 只是为了保存相关信息(Cookie等)
session.get(url=url, headers=headers)

url1 = 'https://cn.bing.com/ttranslationlookup?&IG=EF5190CC19574ED091DB70AFEE20803E&IID=translator.5036.4'
data = {
    'from': 'en',
    'to': 'zh-CHS',
    'text': 'hello'
}
res = session.post(url=url, data=data)

print(res.text)