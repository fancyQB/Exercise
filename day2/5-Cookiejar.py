import urllib.request

# 构建一个已经登录过的用户的headers信息
headers = {
    "Host": "www.renren.com",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    # 添加抓包获取的cookie，这个Cookie是保存了密码无需重复登录的用户的Cookie，里面记录了用户名及密码等登录信息（我这里只显示一部分）
    "Cookie": "anonymid=jj8rv253nsy5xk; depovince=ZGQT; _r01_=1; JSESSIONID=abc11ts3xUMZy4_xctRrw; ick=42229478-7df8-4af6-bc9c-5b8053af2988; XNESSESSIONID=f091543d4e3c; jebecookies=42bc106d-091e-4cb9-bec0-c787c40abbd5|||||; ick_login=28a3cdae-0a78-4ab0-9476-70851e56995a; _de=5326364859035B4BB9D2F66C60E5CA77; p=d56d6b5b4d454d9353d0a4a887bd73326; first_login_flag=1; t=cee83ef3af3833f8ad134697c6ded7736; societyguester=cee83ef3af3833f8ad134697c6ded7736; id=966803836; xnsid=94a95753; ln_uact=15926440508; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=76653543-a05b-475d-a00c-3a7c80761ace%7Caac92d8110f62a4769ecb262abec6415%7C1530809460834%7C1; wp_fold=0; ver=7.0; loginfrom=null"
}

# 通过headers里的报头信息（主要是Cookie信息），构建Request对象
request = urllib.request.Request("http://www.renren.com/", headers=headers)
# 直接访问renren主页，服务器会根据headers报头信息（主要是Cookie信息），判断这是一个已经登录的用户，并返回相应的页面
response = urllib.request.urlopen(request)
# 打印响应内容
# print (response.read())
with open('ren.html', 'wb') as fw:
    fw.write(response.read())
