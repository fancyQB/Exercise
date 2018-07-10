import urllib.request

url = 'https://weibo.cn/3386230482/info'

headers = {
    'Cookie':'_T_WM=c92bdf620773ee19ffd77e2427991801; SUB=_2A252OEfIDeRhGeVN41QT8y7Iwz6IHXVVw2mArDV6PUJbkdAKLUT2kW1NTJV5hHSYt2LAznZVGJL2N4BUv8Hr-iEk; SUHB=0auA93fMcuIiX1; SCF=Am04MhYU5zEJtKWO7sm8efETkppKzw0Cvuz4jajGsEP1Djg-Z_lbvHStZmEe_VkTxF6dggTCcGdQ5F82LR1NoJc.; SSOLoginState=1530673048',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0'
}

req = urllib.request.Request(url=url, headers=headers)

res = urllib.request.urlopen(req)

with open('weibo.html', 'wb') as fw:
    fw.write(res.read())