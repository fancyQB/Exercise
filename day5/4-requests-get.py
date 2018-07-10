import  requests

url = 'https://www.baidu.com/s?'
headers = {

    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'

}
payload = {'wd': '你好'}
res = requests.get(url, params=payload, headers=headers )
res.encoding = 'utf-8'
# with open('baidu.html', 'w', encoding='utf-8') as fw:
#     fw.write(res.text)
# print(res.text)
print(res.content) #响应字节类型的数据
print(res.cookies)