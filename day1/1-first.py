import urllib.request
import urllib.parse

# url = 'http://www.baidu.com/?name=中国'
#编码
str1 = urllib.parse.quote('http://www.baidu.com/?name=中国')

# res = urllib.request.urlopen(url=url1)
print(str1)
# print(type(res))

#
str2 = urllib.parse.unquote('www.baidu.com/%3Fname%3D%E4%B8%AD%E5%9B%BD')
print(str2)
