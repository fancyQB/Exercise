import urllib.request
import urllib.parse
kw = input('请输入您要搜索的内容')
kw = urllib.parse.quote(kw)
url = 'https://www.baidu.com/s?wd='+kw
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
}

#构造请求对象
req = urllib.request.Request(url=url, headers=headers)
#发送请求对象
res = urllib.request.urlopen(req)

#保存数据

with open('china.html', 'w', encoding='utf-8') as fw:
    fw.write(res.read().decode('utf-8'))