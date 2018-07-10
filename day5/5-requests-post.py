import json

import requests

url = 'http://fanyi.baidu.com/sug'
headers = {

    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'

}
data = {
    'kw': 'hello'
}

res = requests.post(url=url, data=data, headers=headers)
print(res.text)

#把json字符串串转换为python对象
json_obj = json.loads(res.text)
#把python对象转换为字符串
str = json.dumps(json_obj, ensure_ascii=False)

with open('fanyi.htm', 'w', encoding='utf-8') as fw:
    fw.write(str)