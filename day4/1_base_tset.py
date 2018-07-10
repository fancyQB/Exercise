from bs4 import BeautifulSoup


#创建bs4
bs = BeautifulSoup(open('testXpath.html', encoding='utf-8'), 'lxml')
#找到a标签和title标签
# result = bs.a
print(bs.a)
# print(bs.title.get_text)
print(type(bs.a))
#格式化输出
# print(bs.prettify())


'''
find 方法

'''
print(bs.find('li', class_="tanshui"))
'''
select 根据选择器得到节点对象

此方法返回一个列表 ，列表中放的是对象




'''
