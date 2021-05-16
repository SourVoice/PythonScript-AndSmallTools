import requests
import chardet
import traceback
from lxml import etree


class Downloader(object):
    def __init__(self):

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }

    def download(self, url):

        print('正在下载页面：{}'.format(url))
        try:
            resp = requests.get(url, headers=self.headers)
            resp.encoding = chardet.detect(resp.content)['encoding']
            if resp.status_code == 200:
                return self.xpath_parse(resp.text)
            else:
                raise ConnectionError

        except Exception:
            print('下载页面出错：{}'.format(url))
            traceback.print_exc()

    def xpath_parse(self, resp):
        try:
            page = etree.HTML(resp)
            trs = page.xpath('//div[@id="list"]/table/tbody/tr')
            proxy_list = []
            for tr in trs:
                ip = tr.xpath('./td[1]/text()')[0]
            port = tr.xpath('./td[2]/text()')[0]
            proxy = {
                'proxy': ip + ':' + port
            }
            proxy_list.append(proxy)
            return proxy_list
        except Exception:
            print('解析IP地址出错')
            traceback.print_exc()


if __name__ == '__main__':
    print(Downloader().download('https://www.kuaidaili.com/free/inha/1/'))
