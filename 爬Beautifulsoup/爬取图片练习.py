from bs4 import BeautifulSoup
import requests
# import urllib.request
import sys


# import time


class Download(object):
    def __init__(self):
        self.target = 'https://www.ivsky.com/bizhi/riben_manhua_t4856/'
        self.headers = {
            'user_agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 '
                'Safari/537.36 '
        }

        self.download_urls = []
        self.urls = []
        self.names = []

    def get_download_urls(self):
        req = requests.get(url=self.target, headers=self.headers)
        html = req.text
        bf = BeautifulSoup(html, 'html.parser')
        div = bf.find_all('img')

        for each in div:
            # print(each)
            urls = each.get('src')
            name = each.get('alt')
            self.names.append(name)
            self.urls.append("https:" + urls)

    def write_to_file(self):
        for (each1, each2) in zip(self.urls, self.names):
            req2 = requests.get(each1)
            path = "C://Users/rockstar/Desktop/fiction/image/" + str(each2)
            """
            urllib.request.urlretrieve(each1, path + '.jpeg', download_p)
            time.sleep(1)
            """
            with open(path, 'wb') as f:
                f.write(req2.content)  # write的参数必须是二进制.content可以解决且参数必须是请求


def download_p(block_size, block_num, total_size):
    """
    :param block_size:
    :param block_num:
    :param total_size:
    :return:
    """
    sys.stdout.write("已下载:%.3f%%" % float(block_size * block_num / total_size) + '\r')
    sys.stdout.flush()


"""
def auto_down(urls, path, download_process):
    try:
        urllib.request.urlretrieve(urls, path, download_process)
    except Exception:
        auto_down(urls, path + '.jpeg', download_process)
# 尝试递归判断是否是由于下载内容太少而引发的瞎子啊不完全(看来不是)
"""

if __name__ == '__main__':
    dl = Download()
    dl.get_download_urls()
    dl.write_to_file()
# write_to_file中urlretrieve下载不完整,好像官方不建议使用这个东西,我尝试将图片下载为二进制
# 在上一行之前我还尝试了运用递归下载,并拉长下载时间来修复,但没有效果
