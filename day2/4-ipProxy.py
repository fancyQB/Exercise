
import  urllib.request
# #ip代理
#
# url ='https://www.baidu.com/s?word=ip&ie=utf-8'
#
# headers = {
#
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
#
# }
#
# req = urllib.request.Request(url=url, headers=headers)
#
# handler = urllib.request.HTTPHandler({'http': '112.84.118.65'})
#
# opener = urllib.request.build_opener(handler)
#
# res = opener.open(req)
#
# with open('ip.html', 'wb')as fw:
#     fw.write(res.read())

import requests

# 创建session对象，可以保存Cookie值
ssion = requests.session()

# 处理 headers
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# 3需要登录的用户名和密码
data = {"email":"15926440508", "password":"zq220115"}

# 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
ssion.post("http://www.renren.com/PLogin.do", data = data)

#  ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
response = ssion.get("http://www.renren.com/966803836/profile")

# 打印响应内容
print (response.text)



