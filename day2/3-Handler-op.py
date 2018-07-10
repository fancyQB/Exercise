import urllib.request


#构建一个handler对象
handler = urllib.request.HTTPHandler()
#通过Handler对象构建一个opener对象
opener = urllib.request.build_opener(handler)

url = 'https://www.cnblogs.com/wqhwe/p/5407468.html'
headers ={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0'
}

req = urllib.request.Request(url=url, headers=headers)

res = opener.open(req)#通过opener对象发送请求

# print(res.read().decode('utf-8'))
with open(r'http.html', 'wb') as fw:
    fw.write(res.read())


