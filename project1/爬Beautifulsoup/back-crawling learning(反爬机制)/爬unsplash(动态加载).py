import requests
import urllib.request
import json
import time
import sys


# 动态加载网站


class Download(object):
    def __init__(self):
        self.serve = 'https://unsplash.com/napi/photos?per_page=12&page='
        self.headers = {
            'user - agent': 'Mozilla / 5.0',
            'cookies': 'xp-feedback-loop-v2=experiment; ugid=c968c1576054f8d683dce93a00b8a0f55383362; '
                       'uuid=6aa2efa0-7e3d-11eb-9cd5-b593c4d335e4; xpos={}; '
                       'azk=6aa2efa0-7e3d-11eb-9cd5-b593c4d335e4; azk-ss=true; _ga=GA1.2.269011929.1615008782; '
                       'intercom-id-njw7pl12=6b7fead0-cc3e-4eef-bb1b-4ce93b3f7d2f; '
                       'un_sesh'
                       '=RDR6VWI4ZmdVSmdLL3V6cTVWTW9tMkMwb2kvNzk4WElQQksvL0VYcWhZMDE2QjZ6MmxUeTRPSDg1TEFxOHlPeVNiajlPU3ZPNTdCYkdTRUZ0MXVQbkgrVk5UMHlsZUpkeHBWYmRudjI0eVhacUFCMXVhNEJVcnAwdFVLRkRPL1dlVUpsVW02VW5RMzEzQ081KzRIcGVSSHUvY2hXaEVuQkJ6VkExNy9jS0ZpRjBDQndZK0VlRjkvOENMaDJ6dEZaZ0wraGU0alpONXUwbHhmVkxLWW9QeU5zYjY4S0EwSnR2Nm9OU3hTMCtYWXRqYmVVN0lQVDgxcGZxR3NXaDJ6bU9XUFl4Q3IxRjY3anE1ZGZIaXNxQ0hWbzdFRmxiTXVVTlJ5T3U5VXE4SHM9LS0wUTA4OGxaOHRvMWpRL3RIYVBETlRBPT0=--80cc9ab04b0eab1283a5338253245810dbad2d29; _gid=GA1.2.2109834900.1615854168; lux_uid=161585416760100511; _sp_ses.0295=*; _sp_id.0295=6ee6b685-6efc-4cc0-8e01-ed0a4ba00fc3.1615008782.3.1615854210.1615114751.b4021ea9-ed22-4d17-88ec-ff9bf0d4f9e2 '

        }

        self.urls = []  # 模拟滚动所得的地址,函数中定义了页数
        self.download_urls = []  # 解析json所得的图片下载地址,每页12张图
        self.image_name = []
        self.paths = []

    # 人工创造一个向下滚动的行为
    def create_link(self):
        for i in range(3, 4):
            self.urls.append(self.serve + str(i))

    def get_image_url(self, target):
        req = requests.get(target, self.headers)
        json_data = json.loads(req.text)  # 返回一个列表对象<class 'list'>  但列表中每一行为字典(for each in json_data)\
        # type(each): <class 'dict'>
        for each in json_data:
            if each['alt_description'] is not 'None':
                # print(each['alt_description'])
                # print('---------------------------------------------------------------------', '\n')
                self.image_name.append(each['alt_description'])  # 为图片命名
            elif each['description'] is not 'None':
                # print(each['description'])
                # print("---------------------------------------------------------------------", '\n')
                self.image_name.append(each['description'])  # 为图片命名
            self.download_urls.append(each['links']['download'])
            # print(each['links']['download'] + '\n')

    def write_in(self):
        for each in self.image_name:
            self.paths.append("C:/Users/rockstar/Desktop/fiction/image/" + str(each))
        for (each1, each2) in zip(self.download_urls, self.paths):
            urllib.request.urlretrieve(each1, each2 + '.jpg', self.download_p)
            time.sleep(1)

    @staticmethod
    def download_p(block_size, block_num, total_size):
        """
        :param block_size:
        :param block_num:
        :param total_size:
        :return:
        """
        sys.stdout.write("--已下载:%.1f%%" % float(block_size * block_num / total_size) * 100 + '\r')
        sys.stdout.flush()


if __name__ == '__main__':
    dl = Download()
    dl.create_link()  # 创造了7页
    for each in dl.urls:
        dl.get_image_url(each)
    dl.write_in()
# success!?
# the possess is too slow ,i am still not find a better way to download this
