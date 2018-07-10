import requests
from bs4 import BeautifulSoup

'''
ctrl+r T 替换

'''
session = requests.session()
url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}

res = session.get(url=url, headers=headers)
bs4 = BeautifulSoup(res.text, 'lxml')
img_code_url = 'https://so.gushiwen.org/'+bs4.select('#imgCode')[0]['src']

res1 = session.get(img_code_url)
with open('yanzhengma.png', 'wb') as fw:
    fw.write(res1.content)

img_code = input('请输入验证码:')





url = 'https://so.gushiwen.org/user/login.aspx?from='
data = {
    '__VIEWSTATE': 'Xln8DzOaLY4KbQx0inryjaYRQmMslcOSSAXr8MBVYQbI6Ad8DD/jAg6POGxhmlY+1S/vebbZQyL9ZW1pRu8P9keMCUjrJrTN2IXN+utTrYOE88ZWVslN3SSCGmQ=',
    '__VIEWSTATEGENERATOR': 'C93BE1AE',
    'from': 'http://so.gushiwen.org/user/collect.aspx',
    'email': '446049601@qq.com',
    'pwd': 'zq7229991',
    'code': img_code,
    'denglu': '登录'
}
res1 = session.post(url=url, data=data)
res1.encoding = 'utf-8'
with open('gushi.html', 'w', encoding='utf-8') as fw:
    fw.write(res1.text)
# print(res1.text)