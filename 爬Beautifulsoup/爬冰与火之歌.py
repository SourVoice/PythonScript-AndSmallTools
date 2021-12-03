import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome('C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe', options=chrome_options)


class Dpower(object):
    def __init__(self):
        self.url = 'https://m.yunbtv.com/voddetail/quanlideyouxidiyiji.html'
        self.head = 'https://m.yunbtv.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'Referer': 'https://player.yunb.tv/',
            'Cache - Control': 'no - store, must - revalidate',
            'Pragma': 'no - cache',
            'Expires': '0'
        }
        self.download_url = []
        self.download_pages = []
        self.ts_urls = []
        self.episode = []
        self.driver = driver

    def get_vediopage(self):
        req = requests.get(self.url)
        print(req)
        html = req.text  # success
        bf = BeautifulSoup(html, 'lxml')
        vedios = bf.find_all('ul', class_="clearfix")
        a_hrefs = BeautifulSoup(str(vedios[0]), 'html.parser')
        hrefs = a_hrefs.find_all('a')
        length_ep = len(hrefs)
        for each, i in zip(hrefs, range(length_ep)):
            self.episode.append('第' + str(i) + '集')
            target_ = each.get('href')
            adownload_url = self.head + str(target_)
            self.download_pages.append(adownload_url)
        # print(self.download_pages)

    def get_play_url(self, each_url):
        try:
            driver.get(each_url)  # 获取下载链接
            m3u8_src = driver.find_element_by_xpath('/html[1]/body[1]/section[2]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/iframe[1]').get_attribute('src')
            true_url = str(m3u8_src).split('=')[1]  # 取=右侧
            html = requests.get(true_url).text  # 获取html内容
            http_src = html.split('\n')[2]
            target_url = true_url.split('cn')[0] + 'cn'
            target_url = target_url + http_src
            req = requests.get(target_url).text
            # print(req)
            self.get_ts_list(req)
        except Exception:
            print("error url:", each_url)
        driver.close()

    # @staticmethod
    def get_ts_list(self, req):
        ts_list = re.findall('EXTINF:(.*),\n(.*)\n#', req)
        for each_ts in ts_list:
            self.ts_urls.append(each_ts[1])

    def download_to_file(self, each_episode):
        path = 'C:/Users/rockstar/Desktop/temp/fiction/quanlideyouxi'
        process = 0
        for each in self.ts_urls:
            req = requests.get(each).text.encode('utf-8')
            with open(path + each_episode, 'ab+') as f:
                print('downloading...', str((process + 1) % len(self.ts_urls) * 100) + '%')
                f.write(req)
        print(each_episode + 'been downloaded successfully')


if __name__ == '__main__':
    # req = requests.get('https://video.buycar5.cn/20200922/OSR9Bdth/1000kb/hls/index.m3u8')
    # print(req.text)
    dw = Dpower()
    dw.get_vediopage()
    for each_episode, each_url in zip(dw.episode, dw.download_pages):
        dw.get_play_url(each_url)
        dw.download_to_file(each_episode)
