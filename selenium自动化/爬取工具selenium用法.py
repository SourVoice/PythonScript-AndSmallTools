import time
from selenium import webdriver  # webdriver可以修改User-Agent
import os

"""模拟打开浏览器,并搜索ChromeDriver"""
"""
driver = webdriver.Chrome(
    'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/')
time.sleep(1)  # Let the user actually see something!
#  找到搜索框
search_box = driver.find_element_by_name('q')  # 找到标签中的以name为搜索元素,找到'q'
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(1)  # Let the user actually see something!
driver.quit()
"""

"""导入按键模拟"""
from selenium.webdriver.common.keys import Keys

# 更改请求头:
options = webdriver.ChromeOptions()
options.add_argument(
    'user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) '
    'Chrome/18.0.1025.133 Mobile Safari/535.19"')  # andriod请求

driver = webdriver.Chrome('C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe', options=options)
driver.get('http:\\www.baidu.com')
# os.system("pause")
search_box = driver.find_element_by_xpath('//input[@type="search"]')
search_box.send_keys('google')
search_box.submit()
driver.get(driver.current_url)
target = driver.find_element_by_xpath('//a[@class="new-nextpage-only"]')

target.click()
print(driver.page_source)  # 获取渲染完后的html
"""界面交互,自动滚动到目标位置,其实不用滚动也可以,但有时候会出现意外"""
