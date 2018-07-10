import requests

url = ''

headers = {

    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'

}

res = requests.get(url=url, headers=headers)
