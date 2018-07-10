import requests

url = 'https://www.baidu.com/s'

proxy = {
    'https': '60.205.205.48'   #代理
}

data = {

    'wd': 'ip'

}

headers = {

    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'

}
res = requests.get(url, params=data, headers=headers, proxies=proxy)
res.encoding = 'utf-8'

with open('ip.html', 'w', encoding='utf-8') as fw:
    fw.write(res.text)