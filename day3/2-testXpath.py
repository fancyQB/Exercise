
from lxml import etree
import urllib.request


#获得文档对象
from  lxml import etree
#构建document对象
d_tree=etree.parse('dingwei.html')
# print(d_tree)
#1-获取所有的li节点
# res=d_tree.xpath('//li')
# # #2-获取所有li节点的class属性
# res=d_tree.xpath('//li/@class')
#3-获取每一个ol节点最后一个li节点的文本内容
# res=d_tree.xpath('//ol/li[last()]/text()')
# #3-获取每一个ol节点最后一个li节点的最后一个文本内容
# res=d_tree.xpath('//ol/li[last()]/text()')[2]
#4-拿到http://mi.com值
# res=d_tree.xpath('//div[@class="hh"]/a/@href')[0]
# #5-拿到雷军文本值
# res=d_tree.xpath('//div[@class="hh"]/a/text()')[0]
# #6-找到id为pp的div中ol节点里面class以h开头的li节点
# res=d_tree.xpath('//div[@id="pp"]/ol/li[starts-with(@class,"h")]')
# #7-找到id为pp的div中ol节点里面class以h开头的第2个li节点文本
# res=d_tree.xpath('//div[@id="pp"]/ol/li[starts-with(@class,"h")]/text()')[1]
# print(res)
res = d_tree.xpath('//*[@id="1"]')
print(res)

# url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E7%BE%8E%E5%A5%B3&rsv_pq=8d9f23b70001f999&rsv_t=c2f7vv%2FH3XcnkSYQtUSyIn58I1cc0%2FlJs72HBX9YODPmEqQ0h1U2L%2Bi%2BWFI&rqlang=cn&rsv_enter=0&rsv_sug3=2&rsv_sug1=1&rsv_sug7=100&inputT=5137&rsv_sug4=5137'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# }
#
# req = urllib.request.Request(url=url, headers=headers)
# res = urllib.request.urlopen(req)
#
# with open('dingwei.html', 'wb') as fw:
#     fw.write(res.read())