import time
from selenium import webdriver


option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
# option.add_argument('headless')

driver = webdriver.Chrome(chrome_options=option)

url = 'https://movie.douban.com/tag/#/'
driver.get(url)
time.sleep(2)
# driver.find_element_by_link_text("设置")[0].click()
while driver.find_element_by_xpath('//div[@id="app"]/div/div/a'):
    driver.find_element_by_xpath('//div[@id="app"]/div/div/a').click()
    time.sleep(2)
