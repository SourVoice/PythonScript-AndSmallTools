"""利用selenium爬取不连续加载的页面"""
import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Download(object):

    def __init__(self):
        self.url = 'https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html'

        self.option = webdriver.ChromeOptions()
        self.option.add_argument(
            '--user-agent=Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) '
            'Version/5.1 Mobile/9A334 Safari/7534.48.3')
        self.driver = webdriver.Chrome('C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe',
                                       options=self.option)

    def get_target_text(self):
        self.driver.get(self.url)

        target1 = self.driver.find_element_by_xpath(
            '//div[@id="app"]/*//div[@class="reader-wrap"]//div[@class="fold-page-text"]//span[@class="read-all"]')

        target2 = self.driver.find_element_by_xpath(
            '//div[@id="passort-login-pop"]/div[@class="tang-title tang-title-dragable"]/a[@class="close-btn"]')
        target2.click()

        target3 = self.driver.find_element_by_xpath(
            '//div[@class="wui-messagebox-wrap goto-app-univ"]//div[@class="inner-wrap"]//div['
            '@class="btns-wrap"]//div[@id="wui-messagebox-cancel-1"]')

        target3.click()


if __name__ == '__main__':
    dl = Download()
    dl.get_target_text()
