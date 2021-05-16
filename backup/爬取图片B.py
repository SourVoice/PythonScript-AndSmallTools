from bs4 import BeautifulSoup
import urllib.request
import requests
import sys


def callback(blocknum, blocksize, totalsize):
    """
    :param blocknum: 已下载数据块
    :param blocksize: 数据块大小
    :param totalsize: 远程文件大小
    :return:
    """
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print('%.2f%%' % percent)
    '''
    sys.stdout.write("--已下载:%.3f%%" % float(float(blocknum) * float(blocksize) / float(totalsize)) + '\r')
    sys.stdout.flush()


if __name__ == '__main__':
    target = 'https://baijiahao.baidu.com/s?id=1662783963649610289&wfr=spider&for=pc'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html, 'html.parser')
    div = bf.find_all('div', class_='img-container')
    a = BeautifulSoup(str(div[0]), 'html.parser')
    a_div = a.find('img', class_='large')
    url = a_div.get('src')

    image_name = url.split('=')[-1]
    path = 'C:/Users/rockstar/Desktop/fiction/' + image_name
    urllib.request.urlretrieve(url, path, callback)



