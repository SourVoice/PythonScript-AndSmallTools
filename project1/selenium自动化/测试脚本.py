from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
driver.get('https:/www.baidu.com/')
search_box = driver.find_element_by_xpath('//*[@name="wd"]')
search_box.send_keys('what?')
search_box.submit()
driver.get(driver.current_url)
targets = driver.find_elements_by_tag_name('a')
tags = 1
for target in targets:
    print(target)


    if target.get_attribute('target') == '_blank':
        target.click()
        time.sleep(2)
