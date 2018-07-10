import requests

session = requests.Session()
url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&logsubmit=yes'

headers ={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}
session.get(url=url,headers=headers)

#以下是post请求
post_url ='http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LY3Ax'

data ={
    'formhash':'dd654965',
    'referer':'http%3A%2F%2Fbbs.chinaunix.net%2F',
    'username':'KevinSun2009',
    'password':'201999gD',
    'loginsubmit':'true',
    'return_type':''
}

res=session.post(url=post_url,data=data)
res.encoding='utf-8'

with open('20-94China.html','w') as fw:
    fw.write(res.text)