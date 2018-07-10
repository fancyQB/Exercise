import time
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
# option.add_argument('headless')

driver = webdriver.Chrome(chrome_options=option)

url ="https://www.toutiao.com/"
driver.get(url)
time.sleep(2)

driver.save_screenshot('2018-7-9头条1.png')  #截图
# time.sleep(2)
# #模拟js滚动 将滚动条拉倒最下方
# js = 'document.documentElement.scrollTop=10000'
# driver.execute_script(js)
# time.sleep(3)
# html = driver.page_source
# time.sleep(3)
# with open('toutiao.html', 'w', encoding='utf-8') as fw:
#     fw.write(html)
# time.sleep(3)

#将滚动条加载到指定的位置
tag = driver.find_element_by_xpath('//div[@id="hotNewsWrap"]/div[1]/div')
#将滚动条执行到目标位置
driver.execute_script('arguments[0].scrollIntoView()', tag)
time.sleep(2)
driver.save_screenshot('2018-7-9头条2.png')# 截图
time.sleep(2)
html = driver.page_source
print(html)
time.sleep(5)
driver.quit()


