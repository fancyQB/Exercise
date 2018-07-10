

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import ui
import win32api
import win32con

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=option)
driver.get('http://www.baidu.com/')
# driver.get('https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=false&word=%E7%BE%8E%E5%A5%B3&hs=2&pn=0&spn=0&di=252287976392&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&ie=utf-8&oe=utf-8&cl=2&lm=-1&cs=1367913442%2C1399721531&os=1635185604%2C4061766901&simid=0%2C0&adpicid=0&lpn=0&ln=30&fr=ala&fm=&sme=&cg=girl&bdtype=15&oriquery=%E7%BE%8E%E5%A5%B3&objurl=http%3A%2F%2Fhbimg.b0.upaiyun.com%2F225a5f3f75d1d4c59532704782eebd25d323fd801e57a-VlY5c4_fw658&fromurl=ippr_z2C%24qAzdH3FAzdH3Fi7wkwg_z%26e3Bv54AzdH3FrtgfAzdH3F8a8800acm0AzdH3F&gsm=0&islist=&querylist=')

kw_input = driver.find_element_by_id('kw')
kw_input.send_keys('美女')
time.sleep(2)
submit = driver.find_element_by_id('su')
submit.click()
time.sleep(5)

beautiful_girl = driver.find_element_by_xpath('//div[@class="op-img-address-divide-high"]/a[1]/img')
# for g in beautiful_girl:
#     g.driver.f
# beautiful_girl = driver.find_element_by_css_selector('')
# a = beautiful_girl[0]
# a = driver.find_element_by_xpath('//input[@class="bg s_btn"]')

# ActionChains(driver).move_by_offset(10, 50).perform()
ActionChains(driver).move_to_element(beautiful_girl).perform()

time.sleep(1)
ActionChains(driver).context_click(beautiful_girl).perform() #在此元素上单击右键
# ActionChains(driver).click(beautiful_girl).perform()
time.sleep(1)
win32api.keybd_event(26,win32con.KEYEVENTF_KEYUP,0)#75的含义就是键盘的K

# time.sleep(5)
# wait = ui.WebDriverWait(driver, 10)
# wait.until(lambda driver: driver.find_element_by_id('currentImg'))
# haha = driver.find_element_by_id('currentImg')
# ActionChains(driver).context_click(haha).perform() #在此元素上单击右键
# haha.click()
# beautiful_girl.click()
#
# # 加启动配置
#
# option = webdriver.ChromeOptions()
##静默加载 在后台偷偷运行
# option.add_argument('headless')
#
# # 打开chrome浏览器
#
# driver = webdriver.Chrome(chrome_options=option)
#
# driver.get("https://www.baidu.com")