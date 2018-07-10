import urllib.parse
import urllib.request

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?'

headers = {

    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'

}

data ={
    'cname': '北京',
    'pid': '',
    'pageIndex': '1',
    'pageSize': '10'
}


data= urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url=url, headers=headers, data=data)

res = urllib.request.urlopen(req)

print(res.read().decode('utf-8'))
