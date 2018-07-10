import urllib.request

import os
from bs4 import BeautifulSoup

url = 'https://www.qiushibaike.com/text/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
}


req = urllib.request.Request(url=url, headers=headers)
res = urllib.request.urlopen(req)

bs = BeautifulSoup(res.read(), 'lxml')
piurl = bs.select('#content-left a > img')[0]
piurl2 = bs.select('#content-left a > img')[0].attrs.get('src')
img_url = 'https:' + piurl2


def download_img(img_url):
    dir_path = './qiubai'
    # 获得基本的文件名
    img_name = os.path.basename(img_url)
    file_path = os.path.join(dir_path, img_name)
    # 下载
    urllib.request.urlretrieve(img_url, file_path)
    print(file_path + '下载完毕')


download_img(img_url)

print(piurl)
print(piurl2)

