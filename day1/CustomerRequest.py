#自定义请求（高级请求）
import urllib.request

url = 'http://www.baidu.com'
# str = urllib.request.urlopen(url=url)
#
# print(str.getheaders())

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 '
}
#构建请求
req = urllib.request.Request(url=url, headers=headers)

#发送请求
res=urllib.request.urlopen(req)
print(res.read().decode('utf-8'))