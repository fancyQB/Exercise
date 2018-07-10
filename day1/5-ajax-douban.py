import urllib

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

headers = {

    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'

}

page= int(input('请输入要查看的页码：'))

start = (page-1)*20
limit = 20

data={
    'start': start,
    'limit': limit
}

data = urllib.parse.urlencode(data)

url = url+data

#构建请求对象
req = urllib.request.Request(url=url, headers=headers, data=data)
#发送请求
res = urllib.request.urlopen(req)
# 读取数据
result = res.read().decode('utf-8')