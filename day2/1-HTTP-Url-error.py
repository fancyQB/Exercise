import urllib.request

url = 'https://blog.csdn.net/whd526/article/details/52279108'

headers ={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}

req = urllib.request.Request(url=url, headers=headers)