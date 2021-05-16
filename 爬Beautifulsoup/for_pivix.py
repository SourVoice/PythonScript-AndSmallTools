# -*- coding:utf-8 -*-
# created by zfq
# first edited: 2016.12.08
import requests
import re
import os

s = requests.Session()


class Pixiv:

    def __init__(self):

    self.baseUrl = "https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index"
    self.LoginUrl = "https://accounts.pixiv.net/api/login?lang=zh"
    self.firstPageUrl = 'http://www.pixiv.net/member_illust.php?id=7210261&type=all'
    self.loginHeader = {
        'Host': "accounts.pixiv.net",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36",
        'Referer': "https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'Connection': "keep-alive"
    }
    self.return_to = "http://www.pixiv.net/"
    self.pixiv_id = '7xxxxxxxx.com',
    self.password = 'xxxxxxx'
    self.postKey = []

    # 獲取此次session的post_key
    def getPostKey(self):
        loginHtml = s.get(self.baseUrl)
        pattern = re.compile('<input type="hidden".*?value="(.*?)">', re.S)
        result = re.search(pattern, loginHtml.text)
        self.postKey = result.group(1)

    # 獲取登陸後的頁面
    def getPageAfterLogin(self):
        loginData = {"pixiv_id": self.pixiv_id, "password": self.password, 'post_key': self.postKey, 'return_to': self.return_to}
        s.post(self.LoginUrl, data=loginData, headers=self.loginHeader)
        targetHtml = s.get(self.firstPageUrl)
        return targetHtml.text

    # 獲取頁面
    def getPageWithUrl(self, url):
        return s.get(url).text

    #   獲取下一頁url
    def getNextUrl(self, pageHtml):
        pattern = re.compile('<ul class="page-list.*?<span class="next.*?href="(.*?)" rel="next"', re.S)
        url = re.search(pattern, pageHtml)
        if url:
        # 如果存在，則返回url
        nextUrl = 'http://www.pixiv.net/member_illust.php'
        str(url.group(1))
        return nextUrl

        else:
        return None

    # 獲取每一頁每一張圖片的詳細頁面地址
    def getImgDetailPage(self, pageHtml):
        pattern = re.compile('<li class="image-item.*?<a href="(.*?)" class="work  _work.*?</a>', re.S)
        imgPageUrls = re.findall(pattern, pageHtml)
        return imgPageUrls

    # 下載指定url的圖片
    def getBigImg(self, sourceUrl, wholePageUrl, name):
        header = {
            'Referer': wholePageUrl,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
        }
        imgExist = os.path.exists('/home/zfq/workspace/Pixiv/QianYe/images/'
        name
        '.jpg')
        if (imgExist):
            print
        u'該圖片已經存在，不用再次儲存，跳過！'
        else:
        img = s.get(sourceUrl, headers=header)
        f = open(name
        '.jpg', 'wb')  # 寫入多媒體檔案要 b 這個引數
        f.write(img.content)  # 多媒體檔案要是用conctent！
        f.close()

    # 開啟圖片詳細頁面，獲得圖片對應的最大解析度圖片
    def getImg(self, pageUrls):

    # 查詢本頁面內最大解析度的圖片的url的正規表示式
    pattern = re.compile('<div class="_illust_modal.*?<img alt="(.*?)".*?data-src="(.*?)".*?</div>', re.S)
    for pageUrl in pageUrls:
    # 之前查詢得到的只是圖片頁面的半截url，這裡加上字首使之完整
    wholePageUrl = 'http://www.pixiv.net'
    str(pageUrl)
    pageHtml = self.getPageWithUrl(wholePageUrl)
    result = re.search(pattern, pageHtml)  # 如果這個頁面只有一張圖片，那就返回那張圖片的url和名字，如果是多張圖片 那就找不到返回none
    if (result):
        imgName = result.group(1)
    imgSourceUrl = result.group(2)
    print
    u'這個地址含有1張圖片，地址：'
    wholePageUrl
    print
    u'正在獲取第1張圖片.....'
    print
    u'名字: '
    result.group(1)
    print
    '源地址：'
    result.group(2)
    self.getBigImg(imgSourceUrl, wholePageUrl, imgName)

    print
    'Done!'

    print
    '--------------------------------------------------------------------------------------------------------'
    else:
    self.getMultipleImg(wholePageUrl)  # 否則執行多張圖片時的特殊處理方法


# 多張圖片的處理方法
def getMultipleImg(self, wholePageUrl):
    imgAlmostSourceUrl = str(wholePageUrl).replace("medium", "manga")


pageHtml = self.getPageWithUrl(imgAlmostSourceUrl)
totalNumPattern = re.compile('<span class="total">(\d)</span></div>', re.S)  # 找到這一頁共有幾張圖
totalNum = re.search(totalNumPattern, pageHtml)
# 執行了一段時間報錯，因為動圖這裡處理不了，實在沒精力了，暫時不抓動圖了吧。。。
if (totalNum):
    print
u'這個地址含有'
totalNum.group(1)
u'張圖片，轉換後的地址：'
str(imgAlmostSourceUrl)
urlPattern = re.compile('<div class="item-container.*?<img src=".*?".*?data-src="(.*?)".*?</div>', re.S)
namePattern = re.compile('<section class="thumbnail-container.*?<a href="/member_illust.*?>(.*?)</a>', re.S)
urlResult = re.findall(urlPattern, pageHtml)
nameResult = re.search(namePattern, pageHtml)
for index, item in enumerate(urlResult):
    print
u'正在獲取第'
str(index1)   u'張圖片......'
printu'名字: '
nameResult.group(1)
str(index
1)
print
u'源地址：'
item
self.getBigImg(item, wholePageUrl, nameResult.group(1)
str(index
1))
print
'Done!'
print
'--------------------------------------------------------------------------------------------------------'
else:
print
u'這個網址是一個gif，實在沒精力去研究怎麼儲存動圖了。。跳過吧'
print
'Done!'
print
'--------------------------------------------------------------------------------------------------------'


# 輸入資料夾名，建立資料夾
def mkdir(self, path):
    path = path.strip()


isExists = os.path.exists(os.path.join("/home/zfq/workspace/Pixiv/QianYe", path))
if not isExists:
    print
u'建了一個名字叫做'
path
u'的資料夾！'
os.makedirs(os.path.join("/home/zfq/workspace/Pixiv/QianYe", path))
return True
else:
print
u'名字叫做'
path
u'的資料夾已經存在了！'
return False


def start(self):
    pathName = 'images'

    self.mkdir(pathName)  # 呼叫mkdir函式建立資料夾！這兒path是資料夾名
    os.chdir(pathName)  # 切換到目錄
    self.getPostKey()  # 獲得此次會話的post_key
    firstPageHtml = self.getPageAfterLogin()  # 從第一頁url開始
    imgPageUrls = self.getImgDetailPage(firstPageHtml)  # 獲取第一頁所有圖片url
    self.getImg(imgPageUrls)  # 獲取第一頁所有圖片url所指向頁面的一張或多張圖片
    currentPageUrl = self.getNextUrl(firstPageHtml)
    while (currentPageUrl):
        currentPageHtml = self.getPageWithUrl(currentPageUrl)
    imgPageUrls = self.getImgDetailPage(currentPageHtml)
    self.getImg(imgPageUrls)
    currentPageUrl = self.getNextUrl(currentPageHtml)


p = Pixiv()
p.start()
